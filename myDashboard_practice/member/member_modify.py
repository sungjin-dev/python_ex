from member import member_service
import session
from util import util_time 
import config as root_config

class ModifymemberData:
    def __init__ (self):
        self.members ={}

    def modifying(self):

        mPw = input('Input member PW: ')
        mMail = input('Input member MAIL: ')
        mPhone = input('Input member PHONE: ')

        self.members = member_service.MemberService().load_members()

        memberFormodify = self.members[session.getSigninedMemberId()]

        memberFormodify['mPw'] = mPw
        memberFormodify['mMail'] = mMail
        memberFormodify['mPhone'] = mPhone
        memberFormodify['mModDate'] = util_time.getCurrentDateTime()

        member_service.MemberService().save_members(self.members)

        print(f'MODIFY SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_members(): {member_service.MemberService().load_members()}')