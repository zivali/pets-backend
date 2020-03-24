from app import db


class Pets(db.Model):
    __tablename__ = 'pets'

    animal_id = db.Column(db.Integer, primary_key=True)
    animal_subid = db.Column(db.String())
    animal_area_pkid = db.Column(db.Integer)
    animal_shelter_pkid = db.Column(db.Integer)
    animal_place = db.Column(db.String())
    animal_kind = db.Column(db.String())
    animal_sex = db.Column(db.String())
    animal_bodytype = db.Column(db.String())
    animal_colour = db.Column(db.String())
    animal_age = db.Column(db.String())
    animal_sterilization = db.Column(db.String())
    animal_bacterin = db.Column(db.String())
    animal_foundplace = db.Column(db.String())
    animal_title = db.Column(db.String())
    animal_status = db.Column(db.String())
    animal_remark = db.Column(db.String())
    animal_caption = db.Column(db.String())
    animal_opendate = db.Column(db.String())
    animal_closeddate = db.Column(db.String())
    animal_update = db.Column(db.String())
    animal_createtime = db.Column(db.String())
    shelter_name = db.Column(db.String())
    album_file = db.Column(db.String())
    album_update = db.Column(db.String())
    cDate = db.Column(db.String())
    shelter_address = db.Column(db.String())
    shelter_tel = db.Column(db.String())

    def __init__(self, animal_id, animal_subid, animal_area_pkid, animal_shelter_pkid, animal_place, animal_kind, animal_sex, animal_bodytype, animal_colour, animal_age, animal_sterilization, animal_bacterin, animal_foundplace, animal_title, animal_status, animal_remark, animal_caption, animal_opendate, animal_closeddate, animal_update, animal_createtime, shelter_name, album_file, album_update, cDate, shelter_address, shelter_tel):
        self.animal_id = animal_id
        self.animal_subid = animal_subid
        self.animal_area_pkid = animal_area_pkid
        self.animal_shelter_pkid = animal_shelter_pkid
        self.animal_place = animal_place
        self.animal_kind = animal_kind
        self.animal_sex = animal_sex
        self.animal_bodytype = animal_bodytype
        self.animal_colour = animal_colour
        self.animal_age = animal_age
        self.animal_sterilization = animal_sterilization
        self.animal_bacterin = animal_bacterin
        self.animal_foundplace = animal_foundplace
        self.animal_title = animal_title
        self.animal_status = animal_status
        self.animal_remark = animal_remark
        self.animal_caption = animal_caption
        self.animal_opendate = animal_opendate
        self.animal_closeddate = animal_closeddate
        self.animal_update = animal_update
        self.animal_createtime = animal_createtime
        self.shelter_name = shelter_name
        self.album_file = album_file
        self.album_update = album_update
        self.cDate = cDate
        self.shelter_address = shelter_address
        self.shelter_tel = shelter_tel

    def serialize(self):
        return {
            'animal_id': self.animal_id,
            'animal_subid': self.animal_subid,
            'animal_area_pkid': self.animal_area_pkid,
            'animal_shelter_pkid': self.animal_shelter_pkid,
            'animal_place': self.animal_place,
            'animal_kind': self.animal_kind,
            'animal_sex': self.animal_sex,
            'animal_bodytype': self.animal_bodytype,
            'animal_colour': self.animal_colour,
            'animal_age': self.animal_age,
            'animal_sterilization': self.animal_sterilization,
            'animal_bacterin': self.animal_bacterin,
            'animal_foundplace': self.animal_foundplace,
            'animal_title': self.animal_title,
            'animal_status': self.animal_status,
            'animal_remark': self.animal_remark,
            'animal_caption': self.animal_caption,
            'animal_opendate': self.animal_opendate,
            'animal_closeddate': self.animal_closeddate,
            'animal_update': self.animal_update,
            'animal_createtime': self.animal_createtime,
            'shelter_name': self.shelter_name,
            'album_file': self.album_file,
            'album_update': self.album_update,
            'cDate': self.cDate,
            'shelter_address': self.shelter_address,
            'shelter_tel': self.shelter_tel,
        }
