class Producer(object):
    def __init__(self):
        pass

    @staticmethod
    def get_request(request):
        if len(request['url']) == 0:
            raise Exception("[-] ERROR: Your url is empty. \n"
                            "Confirm your url is a correct one.")
        if len(request['contributor']) == 0:
            raise Exception("[-] No contributor")
        tag_length = len(request['tag'].split('/'))
        if tag_length != 2:
            if tag_length < 2:
                print("tag_length < 2")
            else:
                print("tag_length > 2")

        conf = {
            'url': request["url"],
            "title": "",
            "contributor": request["contributor"],
            "pdf_filename": "",
            "pdf_buffer": bytes(),
            "tag": request["tag"]
        }
        return conf

    @staticmethod
    def set_request(url, contributor, tag):
        request = {
            'url': url,
            'contributor': contributor,
            'tag': tag
        }
        return request
