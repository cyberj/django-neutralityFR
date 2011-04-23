from django.shortcuts import render_to_response

class DuctTapeMiddleware():
    def process_request(self, request):
        """Block some IPs in name of "Fair net"
        """
        ips = []
        ips.extend("80.118.139.%s" % x for x in range(160, 192))
        ips.extend("62.160.71.%s" % x for x in range(0, 256))
        ips.extend("84.223.174.%s" % x for x in range(48, 64))
        if request.META['REMOTE_ADDR'] in ips:
            return render_to_response("neutralityFR/sorry.html", {})
