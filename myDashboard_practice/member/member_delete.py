from member import member_service
import session
import config as root_config

class DeleteUser:
    def __init__ (self):
        self.members = {}

    def delete(self):
        confirm = input('정말 탈퇴하시겠습니까? [Y] or [N]')

        if confirm == 'Y':
            self.members = member_service.MemberService().load_members()
            del self.members[session.getSigninedMemberId()]
            member_service.MemberService().save_members(self.members)
            session.setSigninedMemberId()
            print('DELETE SUCCESS')

        if root_config.DEV_MOD:
            print(f'self.load_members(): {member_service.MemberService().load_members()}')
