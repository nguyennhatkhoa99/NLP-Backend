# NLP-Backend
If run in localhost check file at ./api/__init__.py line 39 and replace
engine = create_engine(url = "postgresql://postgres:khoa@postgres:5432/chat", echo=True)
-> engine = create_engine(url = "postgresql://postgres:khoa@localhost:5432/chat", echo=True)
# Start postgres
## Pull image
```docker pull postgres```
## Create network
```docker network create nlp-network```
## Run
docker run -p 5432:5432 -e POSTGRES_DB=chat -e POSTGRES_PASSWORD=khoa -e POSTGRES_USER=postgres --network nlp-network --name postgres postgres
# Build and Run Backend
## Build
```docker build -t backend .```
## Run
```docker run -p 5000:5000 --name backend --network nlp-network backend```
