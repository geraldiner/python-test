###
# Read all the comment_ids from another file
# For each comment_id request the info from the API
# Save the response in the txt as a list of dictionaries, [ {}, {} ]
###

import requests

# outputFile = open('comment_info.txt', 'a')
# outputFile.write('number,author,body,permalink,score\n')

outputFile2 = open('comment_info_response.txt', 'a')
count = 1

for id in comment_ids:
    url = 'https://api.pushshift.io/reddit/comment/search?ids=' + id + '&fields=author,body,id,permalink,score'

    headers = {'cache-control': 'no-cache'}

    response = requests.request('GET', url, headers=headers)
    data = response.json()['data'][0]
    outputFile2.write(str(data) + ',\n')
    # author = data['author'].strip()
    # body = data['body'].strip()
    # permalink = 'https://reddit.com/' + data['permalink'].strip()
    # score = data['score']
    # outputFile.write(
    #     str(count) + ',' + author + ',' + body + ',' + permalink + ',' +
    #     str(score) + '\n')
    # count += 1

# outputFile.close()
outputFile2.close()

# outputFile = open('clean_comment_info.txt', 'w')
# inputFile = open('comment_info.txt', 'r')
# for line in inputFile:
#     outputFile.write(line.strip() + '\n')

# outputFile.close()
# inputFile.close()