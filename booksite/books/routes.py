from flask import render_template, request, redirect, url_for, Blueprint, flash, session, jsonify
from flask_login import login_required

from booksite.app import db

from booksite.books.models import Book
from booksite.books.bookForm import BookForm

from booksite.scripts.isbn_scraping import get_ISBN_data

books = Blueprint('books', __name__, template_folder='templates')

@books.route('/')
@login_required
def index():
    if request.method == 'GET':
        if session["userRoll"] == "admin":
            all_books = Book.query.all()
        else:
            #all_books = db.session.execute(text('SELECT * FROM buecher WHERE schlagw != "versteckt"'))
            all_books = Book.query.filter(Book.schlagw != "versteckt").all()
        return render_template("books/book_overview.html", all_books=all_books)

def addBookOverForm(book_form, db):
    # adding a new Book to the DB
    book = Book(autor=book_form.autor.data,
                titel=book_form.titel.data,
                genre=book_form.genre.data,
                subgenreRomane=book_form.subgenreRomane.data,
                format=book_form.format.data,
                verlag=book_form.verlag.data,
                laenge=book_form.laenge.data,
                isbn=book_form.isbn.data,
                jahr=book_form.jahr.data,
                preis=book_form.preis.data,
                standort=book_form.standort.data,
                inhaltsangabe=book_form.inhaltsangabe.data,
                bemerkungen=book_form.bemerkungen.data,
                subtitel=book_form.subtitel.data,
                subgenreSachbuchRatgeber=book_form.subgenreSachbuchRatgeber.data,
                subgenreRatgeber=book_form.subgenreRatgeber.data,
                auflage=book_form.auflage.data,
                schlagw=book_form.schlagw.data,
                bild=book_form.bild.data)
    db.session.add(book)
    db.session.commit()

def alterBookOverForm(book, book_form, db):
    # Update the book fields with the form
    book.autor = book_form.autor.data
    book.titel = book_form.titel.data
    book.genre = book_form.genre.data
    book.subgenreRomane = book_form.subgenreRomane.data
    book.format = book_form.format.data
    book.verlag = book_form.verlag.data
    book.laenge = book_form.laenge.data
    book.isbn = book_form.isbn.data
    book.jahr = book_form.jahr.data
    book.preis = book_form.preis.data
    book.standort = book_form.standort.data
    book.inhaltsangabe = book_form.inhaltsangabe.data
    book.bemerkungen = book_form.bemerkungen.data
    book.subtitel = book_form.subtitel.data
    book.subgenreSachbuchRatgeber = book_form.subgenreSachbuchRatgeber.data
    book.subgenreRatgeber = book_form.subgenreRatgeber.data
    book.auflage = book_form.auflage.data
    book.schlagw = book_form.schlagw.data
    book.bild = book_form.bild.data
    db.session.commit()

@books.route('/book_add', methods=['GET', 'POST'])
@login_required
def book_add():
    if session["userRoll"] != "admin":
        flash("insufficient rights")
        return redirect(url_for('core.index'))
    else:
        book_form = BookForm()
        if request.method == 'GET':
            return render_template("books/book_add.html", form=book_form)
        elif request.method == 'POST':
            addBookOverForm(book_form=book_form, db=db)
            return  redirect(url_for('core.index'))
        return {f"ERROR: Book nr. {book_form.nummer} was not addet."}

@books.route('/book_details/<nummer>', methods=['GET', 'POST'])
@login_required
def book_details(nummer):
    book = Book.query.filter(Book.nummer == nummer).first()
    book_form = BookForm(obj=book)
    if request.method == 'GET':
        return render_template('books/book_details.html', book=book, form=book_form)
    elif request.method == 'POST':
        if book:
            alterBookOverForm(book=book, book_form=book_form, db=db)
        return redirect(url_for('core.index'))

@books.route('/book_delete/<nummer>', methods=['DELETE'])
@login_required
def book_delete(nummer):
    book = Book.query.filter(Book.nummer == nummer).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return {f"Book nr. {nummer} deleted."}, 200
    return {f"ERROR: Book nr. {nummer} was not deleted."}, 404

@books.route('/get_isbn_data', methods=['POST'])
@login_required
def get_isbn_data():
    #isbn = request.json.get('isbn')
    #if not isbn:
    #    return jsonify({'error': 'ISBN is required'}), 400
#
    #try:
    #    book_data = get_ISBN_data(isbn)
    #    return jsonify(book_data)
    #except Exception as e:
    #    return jsonify({'error': str(e)}), 500
    bookdata = {'Title': 'Der Herr der Ringe\nIn der überarbeiteten Übersetzung von Wolfgang Krege | Filmausgabe zur Serie Die Ringe der Macht\nvon J.R.R. Tolkien, aus dem Englischen übersetzt von Wolfgang Krege Der Herr der Ringe In der überarbeiteten Übersetzung von Wolfgang Krege | Filmausgabe zur Serie Die Ringe der Macht', 'Url': 'https://www.isbn.de/buch/9783608987010/der-herr-der-ringe', 'Einband': 'Softcover', 'Laenge': '1568 Seiten', 'Auflage': '1. Auflage 2022', 'Verlag': 'Klett-Cotta', 'Autor': 'J.R.R. Tolkien', 'erschienen am': '02.09.2022', 'ISBN-10': '3-608-98701-0', 'ISBN-13': '978- 3- 608- 98701- 0', 'Maße': '19,5 12,5 1201 gr', 'Lieferstatus': 'verfügbar', 'Preis': '35,00€', 'Erscheinungsdatum': '02.09.2022', 'Beschreibung': '»Ein Ring, sie zu knechten, sie alle zu finden, ins Dunkel zu treiben und ewig zu binden.« Dreibändige Ausgabe zur Serienverfilmung Vor unvordenklichen Zeiten wurden die Ringe der Macht von den Elben geschaffen und Sauron, der Dunkle Herrscher, schmiedete heimlich den Einen Ring und füllte ihn mit seiner Macht, auf dass er über alle anderen Ringe und ihre Träger gebieten konnte. Der Eine Ring wurde Sauron im Lauf der Zeit genommen und so sehr er ihn auch in ganz Mittelerde suchte, er blieb dennoch für ihn verloren. Zeitalter später fällt der Ring in die Hände des Hobbits Bilbo Beutlin, der ihn an seinen Neffen Frodo weitergibt … und so beginnt das größte und gefährlichste Abenteuer der Fantasyliteratur. Im ersten Band »Die Gefährten« bekommt der junge Frodo in einem ruhigen Dorf im Auenland ein Geschenk, das sein Leben für immer verändern wird – den Einen Ring, der seit Jahrhunderten als verschollen galt. Ein mächtiges und furchterregendes Ding, mit dem der Dunkle Herrscher einst Mittelerde versklavte.\xa0Nun erhebt sich die Dunkelheit erneut, und Frodo muss tief in das Reich des Dunklen Herrschers vordringen, bis zu dem einzigen Ort, an dem der Ring zerstört werden kann: dem Schicksalsberg.\xa0Die Reise wird Frodos Mut, seine Freundschaften und sein Herz auf die Probe stellen. Denn der Ring korrumpiert alle, die ihn tragen. Kann Frodo den Ring vernichten, bevor der Ring ihn vernichtet? In »Die zwei Türme« , dem zweiten Band, sind die Gefährten verstreut. Einige bereiten sich auf den Krieg gegen den Dunklen Herrscher vor, einige stellen sich dem Verrat des verderbten Zauberers Saruman entgegen. Nur Frodo und Sam sind übrig, um den verfluchten Ring in den Feuern des Schicksalsberges zu vernichten.\xa0Der Schicksalsberg liegt im Herzen des Reiches des Dunklen Herrschers. Ihr einziger Führer auf der gefährlichen Reise dorthin ist Gollum, eine hinterlistige und besessene Kreatur, die einst den Ring besaß und sich entsetzlich danach sehnt, ihn wieder zu kriegen. Als sich die dunklen Mächte sammeln, liegt das Schicksal von Mittelerde in den Händen von zwei einsamen Hobbits. Wird Gollum sie in den Tod führen? Im dritten und letzten Band »Die Rückkehr des Königs« ist der Dunkle Herrscher auferstanden. Und während er Horden von Orks entfesselt, um ganz Mittelerde zu unterwerfen, kämpfen sich Frodo und Sam tief in sein Reich nach Mordor vor. Um Sauron zu besiegen, muss der Eine Ring in den Feuern des Schicksalsberges vernichtet werden. Doch der Weg dorthin ist unvorstellbar schwer, und Frodos Kräfte schwinden. Der Ring macht sich alle, die ihn tragen, untertan und Frodo bleibt kaum noch Zeit. Werden Sam und Frodo ihr Ziel erreichen, oder wird der Dunkle Herrscher am Ende wieder über ganz Mittelerde herrschen?', 'Genre': 'Epische Fantasy (High Fantasy)'}
    return jsonify(bookdata)