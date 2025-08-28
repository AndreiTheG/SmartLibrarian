**Smart Librarian - DavaX**

***Resurse***

- fastapi - The main web framework
- uvicorn - Runs the FastAPI app as a local web server
- pydantic - Data validation & serialization
- sqlalchemy - Providing SQL and ORM (Object Relational Mapping) features for database access
- chromadb - Storing and querying the embeddings for LLM apps
- openai - Providing tools to interact with OpenAI API
- speech_recognition - Used for speech-to-text conversion
- pyttsx3 - Used for text-to-speech conversion

-pip install fastapi uvicorn pydantic sqlalchemy chromadb openai speech_recognition pyttsx3

**Tutorial de utilizare a aplicatiei de chatbot cu rol de Bibliotecar**

***Pasul 1 - Clonarea repository-ului in PyCharm***
Vom clona repo-ul din GitHub in PyCharm folosind comanda:

bash

git clone AndreiTheG/SmartLibrarian

***Pasul 2 - Crearea venv-ului si instalarea pachetelor necesare***

Pentru inceput, user-ul va crea un environment separat (venv) astfel incat acesta sa poata testa si instala local pachetele
Dupa care, pentru ca programul să funcționeze cum trebuie, vom instala următoarele pachete:

- fastapi – pentru framework-ul web FastAPI
- uvicorn – pentru a rula aplicația drept un server web local
- pydantic – pentru serializarea și validarea datelor
- sqlalchemy - pentru a oferi features de acces al bazei de date pentru SQL si ORM (Object Relational Mapping) 
- chromadb - pentru stocarea si interogarea embedding-urilor pentru aplicatiile de tip LLM
- openai - pentru a oferi toolurile de interactiune cu OpenAI API
- speech_recognition - pentru conversia de tip speech-to-text 
- pyttsx3 - pentru conversia de tip text-to-speech

Comanda instalare:

bash

pip install fastapi uvicorn pydantic sqlalchemy chromadb openai speech_recognition pyttsx3


***Pasul 3 - Instalarea framework-urilor de frontend React si Vite***
Pentru a crea si avea acces la UI-ul aplicatiei, trebuie instalat Node.js pentru runtime environment. 
Dupa care, vom instala framework-urile React si Vite din terminal prin urmatoarele comenzi:

bash

npm create vite@latest frontend --template react
cd frontend
npm install


***Pasul 4 - Setarea cheii de OpenAI API***

Pentru a avea acces la conversatie cu Api-ul OpenAI, va fi nevoie sa setam cheia de acces din terminal.


***Pasul 5 - Rularea scripturilor in Python***

****Pasul 5.1 - Rularea scriptului main.py****
Scop: Lansează execuția aplicației, creează și deschide serverul web local, și definește ruta de chat pentru conversatia cu chatbot-ul

****Pasul 5.2 - Modele de input pentru rezumatele cartilor si istoricul chat request-ului****
Pentru a salva datele în baza de date, va fi nevoie să definim structura modelelor de input-uri ale rezumatelor cartilor astfel încât să putem 
verifica dacă datele sunt existente în momentul în care verificăm existența rutelor.
- Cream directorul model
- Adăugăm următoarele modele:
- - 5.2.1 ChatRequest.py
  - 5.2.2 SummaryBook.py
  - 5.2.3 SummaryBookModel.py
 
****Pasul 5.3 - Scriptul Database.py****
Scop: Sa genereze o baza de date SQLite care salveaza datele cartilor cu tot cu titlu si rezumat

****Pasul 5.4 - Executarea metodelor rutelor****
Folosim APIRouter() pentru definirea rutelor GET si POST
- POST - atat pentru inserare si salvare a datelor cartilor, cat si pentru conversatia ch chatbot-ul
- GET - verificare existenta a datelor in functie de id-urile lor

Scopul: 
- o linie specifica de date in functie de id-urile cartilor
- Chat request cu chatbot-ul

  
****Pasul 5.5 - Rularea scriptului load_db_to_chroma.py****
Scop: sa incarce si sa incorcoreze datele din baza de date sub forma de vectori in ChromaDB astfel incat aceste
date sa poata fi folosite in LLM.



****Pasul 5.6 - Rularea scriptului cli_bot.py****
Scop: sa incepem conversatia cu chatbot-ul prin CLI, avand posibilitatea de a alege o optiune de interactiune
cu chatbot-ul fie doar prin text, fie prin metoda speech-to-text, fie prin metoda text-to-speech.

Folosim urmatoarea comanda:

bash

python -m backend.chatbot.cli_bot


***Pasul 6 - Dezvoltarea si testarea frontend-ului***

****Pasul 6.1 - Instalarea librariei axios in directory-ul frontend****
Scop: sa putem accesa request-urile de HTTP.

Comanda:

bash

npm install axios

****Pasul 6.2 - Crearea componentei Chat.jsx****
Vom crea aceasta componenta si o vom importa in fisierul App.jsx, astfel incat sa conectam frontend-ul de server-ul aplicatiei prin url-ul http://localhost:8000/chat, 
sa avem acces si sa se afiseze interfata chat-ului.

***Pasul 7 - Activarea CORS-ului in FastAPI***
Scop: Activam CORS-ul pentru a face legatura cu url-ul frontend-ului "http://localhost:5173" in momentul in care rulam main.py.

***Pasul 8 - Rularea aplicatiei***

****Pasul 8.1 - Rularea server-ului****

Vom rula fisierul main.py astfel incat sa pornim server-ul aplicatiei de tip FastAPI.
Apoi putem accesa Postman sau Swagger, astfel incat sa putem insera si salva datele cartilor in baza de date,
sa accesam un rand de date prin id-ul acestuia, si de a trimite un input de text astfel incat GPT-ul
sa genereze un raspuns, fie ca ii cerem sa ne afiseze rezumatul unei carti, fie sa ne recomande cartile din 
baza de date in functie de genul cartii.

Comanda rulare:

bash

uvicorn backend.main:app --reload

****Pasul 8.1 - Rularea interfetei****

Scop: Sa avem acces si sa putem deschide interfata aplicatiei prin browser. Dupa ce vom rula comanda din terminal,
deschidem browser-ul la "http://localhost:5173"

Comanda rulare:

bash

npm run dev
