import requests,random

def getAnimeChar(id=0):
    if(id==0):
        id=random.randint(1,41999)
    query = '''
    query ($id: Int) {
    Character (id: $id) { 
        id
        name {
        full
        userPreferred
        }
        image {
            large
        }
        age
        dateOfBirth {
            year
            month
            day
        }
        description
        gender
    }
    }
    '''

    # Define our query variables and values that will be used in the query request
    variables = {
        'id': id
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables}).json()

    if(str(response) == "{'errors': [{'message': 'Not Found.', 'status': 404, 'locations': [{'line': 3, 'column': 5}]}], 'data': {'Character': None}}"):
        return -1
    else:
        return response['data']
