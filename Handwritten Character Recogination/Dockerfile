# official python image / sloim image for faster 
FROM python:3.10-slim

#set the working dir inside container  streamlit file
WORKDIR /app            

# Copy dependencies file first (for caching)
COPY requirements.txt .

# install requirements.txt   /  Upgrades pip first, so dependencies install faster
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# Copy the rest of the code
COPY . .     

# expose the streamlit port
EXPOSE 8501  

CMD [ "streamlit","run","app.py","--server.port=8501","--server.address=0.0.0.0" ]
