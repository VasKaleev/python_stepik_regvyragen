from html.parser import HTMLParser
data='<html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Timer ⏲</title><link rel="icon" href="./img/goes.png"><link rel="stylesheet" href="./css/normalize.css"><link rel="stylesheet" href="./css/style.css"></head><body><div class="time_wrapper"><h1 class="bold minutes">1:00:00</h1><img class="time" src="./img/start_end.png"></div><div class="buttons"><button class="buttons_button regular start" onclick="start()">Start</button><button class="buttons_button regular notshow pause" onclick="pause()">Pause</button></div></body>'
class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
        self.text += data

f = HTMLFilter()
f.feed(data)
print(f.text)
