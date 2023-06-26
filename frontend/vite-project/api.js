export const API_URL = 'http://localhost:8000/api/v1/';

export function GET(){
      return {
    url: API_URL + 'proposals/',
    options: {
      method: 'GET',
    },
  };
}
export function POST_PROPOSAL(body){
    console.log('POST_PROPOSAL_', body);
    console.log('POST_PROPOSAL_', JSON.stringify(body));
    return {
        url: API_URL + 'proposals/celery',
        options: {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
            }
        },
        body: JSON.stringify(body)
    };
}

