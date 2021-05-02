def makevideo(video):
    result = {}
    result['comment'] = video[0]
    result['typeid'] = video[1]
    result['play'] = video[2]
    result['pic'] = video[3]
    result['description'] = video[4]
    result['title'] = video[5]
    result['author'] = video[6]
    result['mid'] = video[7]
    result['created'] = video[8]
    result['length'] = video[9]
    result['aid'] = video[10]
    result['bvid'] = video[11]
    result['is_union_video'] = video[12]
    return result
def makevideos(videos):
    result = []
    for video in videos:
        result.append(makevideo(video))
    return result