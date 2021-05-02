const body = new FormData
        body.append("files", "@output_file.txt; type=text/plain")
        body.append("multipleChoice", "true")
        body.append("contentType", "DOCUMENT")


        fetch("https://gateway.flexudy.com/api/v1/wh-quiz/queue", {
            body,
            headers: {
                Accept: "application/json",
                "Content-Type": "multipart/form-data",
                Licensekey: "license-key"
            },
            method: "POST"
        })