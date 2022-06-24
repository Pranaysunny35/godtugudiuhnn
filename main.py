from pyrogram import Client, filters
import time

app = Client(
    "AgCK7XEFiRwHDg9C_mYSmhWo4WKT9ZKpCS4fY5IWZsxF7caXbHTQBy1rnF4trWFCd6IuTpXc8TduVAYHj-aWJkkQACu8NyuzGZYbAV3AAYiwccON2Q9eYPl4pR4Fz01tGjHZ9P678W7WQUvcxNyYR8CjNjjNrq8POjH0sLwrdmmrh_k7PmVeegiXrx0ATzOc3A5hY4YuoYQecaVltiDjbqNWe1mC1tfym-AfTwa-PurDY215DK-hJsXtIUpeyNN2_wLWucfpt75mbDyYMGGIVB_IJFckvzrMnxzkxbZyX4wF0msqOItenQrIPbPk_btAMBdUxugznFqe-DM4S4gYkeYZAAAAATNwjnwA",
    api_id=14952323,
    api_hash="224b9aecbcc210351953f259bdc9720b"
)

@app.on_message(filters.private & filters.text)
def spem(client, message):
    if 'fak' in message.text:

        try:
            n = message.message_id
            client.send_message(
    chat_id=message.chat.id,
    text="/challenge",
    reply_to_message_id=n
)
        except Exception as e:
            client.send_message('bunny', e)
            client.send_message('bunny', message.text)
        
while True:
    try:
        app.run()
    except:
        time.sleep(15)
