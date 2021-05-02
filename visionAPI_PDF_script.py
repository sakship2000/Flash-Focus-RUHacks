import os, io
import re
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
from google.cloud import storage
from google.protobuf import json_format


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'vision-token.json'

client = vision_v1.ImageAnnotatorClient()

def async_detect_document(gcs_source_uri, gcs_destination_uri):
    #OCR with PDF/TIFF as source files on GCS

 # Number of pages grouped into each json output file.
    batch_size = 2
    mime_type = 'application/pdf'
    feature = vision_v1.types.Feature(
        type=vision_v1.enums.Feature.Type.DOCUMENT_TEXT_DETECTION)


    gcs_source = vision_v1.types.GcsSource(uri=gcs_source_uri)
    input_config = vision.types.InputConfig(gcs_source=gcs_source, mime_type=mime_type)
    
    gcs_destination = vision_v1.GcsDestination(uri=gcs_destination)
    output_config = vision_v1.types.OutputConfig(gcs_destination=gcs_dstination, batch_size=batch_size)
    
    async_request = vision_v1.types.AsyncAnnotateFileRequest(
        fatures=[feature], input_config=input_config, output_config=output_config)
    
    operation = client.async_batch_annotate_files(requests=[async_request])
    opreation.result(timeout=180)
    
    #Setting up Google Cloud
    storage_client = storage.Client.from_service_accoun_json('vision-token.json')
    match = re.match(r'gs://([^/]+)/(.+)', gcs_destination_uri)
    bucket_name = match.group(1)
    prefix = match.group(2)
    bucket = storage_client.get_bucket(bucket_name)
    
    # List object with given prefix
    blob_list = list(bucket.list_blobs(prefix=prefix))
    print('Ouput files:')
    for blob in blob_list:
        print(blob.name)
    
    # Process the first output file from GCS.
    output = blob_list[0]
    json_string = output.download_as_string()
    response = json_format.Parse(
        json_string, vision_v1.types.AnnotateFileResponse())
    
    first_page_response = response.response[0]
    annotation = first_page_response.full_text_annotation
    
    # Print the full text from first page.
    print(u'Full text:')
    print(annotation.text)

#Define source and destination uri's
gcs_source_uri = 'gs://pdf_bucket_ruhacks/psych-notes.pdf'
gcs_destination_uri = 'gs://pdf_bucket_ruhacks/pdf_result '

#Call method
async_detect_document(gcs_source_uri, gcs_destination_uri)
