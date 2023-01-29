from famLink.utility.repository import BaseRepository
from .models import Member



class MemberRepository(BaseRepository):
    def _init_(self):
        self.model = Member

    