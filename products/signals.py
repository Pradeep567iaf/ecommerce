# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from products.models import Deposit
# from member.models import User
# from django.db.models import Q


# @receiver(pre_save, sender = Deposit)
# def auto_load_name(sender, instance, *args, **kwargs):
#     data = User.objects.get(username = instance.name )
#     instance.phone_number = data.phone_number
#     instance.member_id = data.member_id
    #
    # instance.member_id = data.member_id




    # def get_name(self):
    #     user_name = User.objects.get(username = self.name).member_id
    #     return user_name