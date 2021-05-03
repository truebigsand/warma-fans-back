import Sqlite3Helper
import requests
import json
def update():
    #try:
    db = Sqlite3Helper.Sqlite3Helper('warma.db')
    db.execute('DELETE FROM videos WHERE aid > 0')
    uid = "53456"
    #info = json.loads(requests.get('https://api.bilibili.com/x/space/acc/info?mid=53456&jsonp=jsonp').text)
    #videos = []
    limit = json.loads(requests.get(f'https://api.bilibili.com/x/space/arc/search?mid={uid}&ps=30&pn=1&jsonp=jsonp').text)['data']['page']['count']
    limit_now = 0
    pageNum = 1
    while limit_now < limit:
        tmp = json.loads(requests.get(f'https://api.bilibili.com/x/space/arc/search?mid={uid}&ps=30&pn={pageNum}&jsonp=jsonp').text)
        for video in tmp['data']['list']['vlist']:
            db.execute('INSERT INTO videos VALUES({},{},{},"{}","{}","{}","{}",{},{},"{}",{},"{}",{})'.format(video['comment'],video['typeid'],video['play'],video['pic'],video['description'],video['title'],video['author'] ,video['mid'],video['created'],video['length'],video['aid'],video['bvid'],video['is_union_video']))
            print('INSERT INTO videos VALUES({},{},{},"{}","{}","{}","{}",{},{},"{}",{},"{}",{})'.format(video['comment'],video['typeid'],video['play'],video['pic'],video['description'],video['title'],video['author'] ,video['mid'],video['created'],video['length'],video['aid'],video['bvid'],video['is_union_video']))
        limit_now += 30
        pageNum += 1
    print(db.query('SELECT * FROM videos'))
    #except:
    #    return '{"msg":"failed"}'
    return '{"msg":"success"}'
if __name__ == '__main__':
    update()
    print(Sqlite3Helper.Sqlite3Helper('warma.db').query('SELECT * FROM videos'))