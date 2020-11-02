from flask import Flask,render_template,request
import os

app=Flask(__name__)
@app.route('/',methods=['GET'])
def homepage():
    return render_template("index.html")
@app.route('/processing',methods=['POST'])
def process():
    if request.method=='POST':
        destination=request.form['selector']
        print(destination)
        os.chdir(destination)
        current=os.getcwd()
        print(current)
        dir=os.listdir(destination)
        if not os.path.exists("Documents"):
            os.makedirs("Documents")
        if not os.path.exists("Musics"):
            os.makedirs("Musics")
        if not os.path.exists("Pictures"):
            os.makedirs("Pictures")
        picture_entensions=[".png",".jpeg",".jpg"]
        documents_extensions=['.doc',".txt",".css","html"]
        musics_extension=[".mp3",".avm",".wav"]
        pic_found_extensions=[]
        document_found_extensions=[]
        musics_found_extensions=[]
        #### For pictures
        for i in dir:
            if os.path.splitext(i)[1].lower() in picture_entensions:
                pic_found_extensions.append(i)

        ## For Documents
        for x in dir:
            if os.path.splitext(x)[1].lower() in documents_extensions:
                document_found_extensions.append(i)
        ## For Musics
        for z in dir:
            if os.path.splitext(z)[1].lower() in musics_extension:
                musics_found_extensions.append(z)
        ### After finding all the file names in their list we have to move this files
        for moving_musics in musics_found_extensions:
            os.replace(moving_musics,f"Musics/{moving_musics}")

        for moving_pictures in pic_found_extensions:
            os.replace(moving_pictures,f"Pictures/{moving_pictures}")
        for moving_documents in document_found_extensions:
            os.replace(moving_documents,f"Documents/{moving_documents}")
        return render_template("index2.html")
    else:
        print("Something Went Wrong")



if __name__=="__main__":
    app.run(debug=True)