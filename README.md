# POS Aligner

This program computes and generates visualizations for optimal local, fitting, and global alignments between strings of text.


## Dependencies:
This project requires many dependencies split among the both the front and backend components. To see all the dependencies, checkout ```API/requirements.txt``` and ```Web/cs466-website/package.json```

To install all dependencies, run: 

```
pip install -r API/requirements.txt
cd Web/cs466-website && npm install
```

## To run this program:

Running this project requires two terminal windows, one for the backend, and one for the front end. 

### Frontend
To run the frontend, ensure nothing is currently running on port 5173. Then, run the following:

```
cd Web/cs466-website
npm run dev
```

Now, you can access your website at localhost:5173

### Backend
To run the frontend, ensure nothing is currently running on port 443. Then, run the following:

```
python3 API/main.py
```


Now, your API endpoints should be available at localhost:443
