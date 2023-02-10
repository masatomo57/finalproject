from flask import Blueprint, render_template, request, redirect
from apps.app import db
from apps.shiori.models import Itinerary
from sqlalchemy.sql import func

import datetime

shiori = Blueprint(
    'shiori',
    __name__,
    template_folder='templates',
    static_folder='./static',
)

@shiori.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        for i in range(1, int(request.form.get("counter"))):
            try:
                currentitinerary = db.session.query(Itinerary).filter_by(id=i).first()
                if not request.form.get(f"itinerary{i}"):
                    raise Exception
                if currentitinerary:
                    currentitinerary.itinerary = request.form.get(f"itinerary{i}")
                    currentitinerary.date = datetime.date(int(request.form.get(f"date{i}")[0:4]), int(request.form.get(f"date{i}")[5:7]), int(request.form.get(f"date{i}")[8:10]))
                    currentitinerary.start = datetime.time(int(request.form.get(f"start{i}")[0:2]), int(request.form.get(f"start{i}")[3:5]))
                    currentitinerary.end = datetime.time(int(request.form.get(f"end{i}")[0:2]), int(request.form.get(f"end{i}")[3:5]))
                    db.session.commit()

                else:
                    newitinerary = Itinerary(
                        itinerary=request.form.get(f"itinerary{i}"),
                        date=datetime.date(int(request.form.get(f"date{i}")[0:4]), int(request.form.get(f"date{i}")[5:7]), int(request.form.get(f"date{i}")[8:10])),
                        start=datetime.time(int(request.form.get(f"start{i}")[0:2]), int(request.form.get(f"start{i}")[3:5])),
                        end=datetime.time(int(request.form.get(f"end{i}")[0:2]), int(request.form.get(f"end{i}")[3:5])),
                    )
                    db.session.add(newitinerary)
                    db.session.commit()
            except:
                if not request.form.get(f"date{i}"):
                    currentitinerary = db.session.query(Itinerary).filter_by(id=i).delete()
                    db.session.commit()


        return redirect("/")
    else:
        Itinerarys_dict = {}
        dates = db.session.query(Itinerary.date).group_by("date").all()
        counter = db.session.query(func.max(Itinerary.id).label('id_max')).one_or_none().id_max
        if not counter:
            counter = 0
        for date in dates:
            Itinerarys_dict[date]=db.session.query(Itinerary).filter_by(date=date["date"]).all()
        return render_template("/shiori/index.html", Itinerarys_dict=Itinerarys_dict, dates=dates, counter=counter+1)

@shiori.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            for i in range(1, int(request.form.get("counter"))):
                if not request.form.get(f"itinerary{i}"):
                    continue
                itinerary = Itinerary(
                    itinerary=request.form.get(f"itinerary{i}"),
                    date=datetime.date(int(request.form.get("date")[0:4]), int(request.form.get("date")[5:7]), int(request.form.get("date")[8:10])),
                    start=datetime.time(int(request.form.get(f"start{i}")[0:2]), int(request.form.get(f"start{i}")[3:5])),
                    end=datetime.time(int(request.form.get(f"end{i}")[0:2]), int(request.form.get(f"end{i}")[3:5])),
                )
                db.session.add(itinerary)
                db.session.commit()
            return redirect("/")
        except:
            validation="全て入力してください"
            return render_template("/shiori/register.html", validation=validation)
    else:
        return render_template("/shiori/register.html")

