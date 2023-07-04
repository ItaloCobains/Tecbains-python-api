import uvicorn
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()

    uvicorn.run("tecbains.api:app", host='0.0.0.0', port=8080, reload=True)
