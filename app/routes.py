from flask import render_template, url_for, redirect, flash
from app.forms import AddItemForm
from app.models import Item
from app import app, db


@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    form = AddItemForm()
    if form.validate_on_submit():
        flash( ' {} added!'.format(form.body.data   ))
        item = Item(body=form.body.data, checked=1)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('index'))

    items = Item.query.all()
    return render_template('index.html',title='Home', form=form, items=items)

@app.route('/delete-item/<int:item_id>', methods=['POST']) #temp name, probably can change to /item/delete
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted from list !!')
    return redirect(url_for('index'))
