message = input(">")

words = message.split(' ') #outputs list of words like['we','now','try']

emojis = {
    ':)' : '😄',
    '):' : '😠',
    '00' : '👀'
}
out_put = ""
for word in words:
    out_put += emojis.get(word,word) + " " #get(key,defaultValue)
print(out_put)
