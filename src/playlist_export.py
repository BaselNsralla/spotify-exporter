from ytmusicapi import YTMusic


raw = """accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-GB,en-US;q=0.9,en;q=0.8
authorization: SAPISIDHASH 1652244674_1a2aab93cc8620e1e73eb2ea0a8876f9c0cfc2ed
cache-control: no-cache
content-length: 2307
content-type: application/json
cookie: CONSENT=YES+srp.gws-20220420-0-RC3.en+FX+385; YSC=4s-RD1znyoA; VISITOR_INFO1_LIVE=qs9GzdABs2k; PREF=tz=Europe.Stockholm&f6=40000000; SID=KAhQEO_0XK-U3Kmc5uedvRX9FUopi4lDyjj1IJZXTGkDeRj1l1jMcfzAasikSLX7LunLeg.; __Secure-1PSID=KAhQEO_0XK-U3Kmc5uedvRX9FUopi4lDyjj1IJZXTGkDeRj1L-q1WaRTMzayiXDIKCRLIw.; __Secure-3PSID=KAhQEO_0XK-U3Kmc5uedvRX9FUopi4lDyjj1IJZXTGkDeRj1QlazeTlKyQsU8Bqra-W1Kg.; HSID=A979IWW_3bCaIbLQ0; SSID=A0uhJcnJpXXKWj1s3; APISID=zJNPLHhnbdM88Bcg/AmcWg7ag_hmV9L0gJ; SAPISID=hqi5Wxs2pwWd0kuO/AKoRL8MivByS8Ts6m; __Secure-1PAPISID=hqi5Wxs2pwWd0kuO/AKoRL8MivByS8Ts6m; __Secure-3PAPISID=hqi5Wxs2pwWd0kuO/AKoRL8MivByS8Ts6m; LOGIN_INFO=AFmmF2swRgIhAI3DtfSOHTsSD3N7eEJaHOteGkoyO4unwmsGpN_fDhw2AiEAoYz01RkYsNDRR1kO1zdE_FLIHlWC2TXGOHSBmrLtmok:QUQ3MjNmd1YxTDl1Q0hQaE9OUnZQVTZiWV9wQlZoM2lEOUpCZzFsd3JyTnBsZFN6TWhDRUIyWUl6SGxrelZxU3VDaGNhTVdCTFdZSGI0NzlyZ2xVU2RCcVlORVhmWGxRN29ha2hjOUFUdEl6eUtoUGNuajJMMEgzZmtwTjdEMzI4cS0wYlVoeXZORUFscXFRdGNZRDd2VEhFTFp0TzhqdTlB; ST-1b=csn=MC42NDkzNjA1NDkwNzc3OTcy&itct=CPwCEMOUBhgEIhMI_KmA8dLW9wIVc8ZPCB0Q8giO; SIDCC=AJi4QfH-6ehMAv8DAWcm8sh-Kp0Dr_kh8B7N8EeGRk4Xh0FADTiFwrKB1LfAt5lDSuAaETrx; __Secure-3PSIDCC=AJi4QfH-ErGs0uMet_GIhUQgsAxnKt_hBch1ZsWSHVRh50ZdFVQJbb2dpXwQYxoHsJOzW5xx
origin: https://music.youtube.com
pragma: no-cache
referer: https://music.youtube.com/channel/UCM6h8_rNLtYVky-6LPjOMIw
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"
sec-ch-ua-arch: "x86"
sec-ch-ua-bitness: "64"
sec-ch-ua-full-version: "97.0.4692.99"
sec-ch-ua-mobile: ?0
sec-ch-ua-model
sec-ch-ua-platform: "macOS"
sec-ch-ua-platform-version: "11.5.1"
sec-fetch-dest: empty
sec-fetch-mode: same-origin
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36
x-client-data: CJe2yQEIprbJAQjEtskBCKmdygEIq//KAQiSocsBCJihywEInvnLAQjnhMwBCJmPzAEIyKbMARisqcoB
x-goog-authuser: 0
x-goog-visitor-id: CgtxczlHemRBQnMyayjogO2TBg%3D%3D
x-origin: https://music.youtube.com
x-youtube-client-name: 67
x-youtube-client-version: 1.20220502.01.00"""

def export_playlist_tracks(playlist):
    ## TODO: Handle no search results
    YTMusic.setup(filepath="headers.json", headers_raw=raw)
    ytmusic = YTMusic('headers.json')
    playlist_name = playlist['name']
    playlist_tracks = playlist['tracks']
    playlistId = ytmusic.create_playlist(playlist_name, "test description")
    
    for track in playlist_tracks:
        search_results = ytmusic.search(track)
        print(search_results)
        ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])


