from django.db import models


class Person(models.Model):

    MAN = 0
    WOMAN = 1

    HOKKAIDO = 0
    TOHOKU = 5
    TOKYO = 10
    CHIBA = 11
    KANAGAWA = 12
    SAITAMA = 13
    TOCHIGI = 14
    IBARAGI = 15
    CHUBU = 20
    KANSAI = 25
    CHUGOKU = 30
    SHIKOKU = 35
    KYUSHU = 40
    OKINAWA = 45

    # 名前
    name = models.CharField(max_length=128)
    # 誕生日
    birthday = models.DateTimeField()
    # 性別
    sex = models.IntegerField(editable=False)
    # 出身地
    address_from = models.IntegerField()
    # 現住所
    current_address = models.IntegerField()
    # メールアドレス
    email = models.EmailField()


class Manager(models.Model):

    # 部署の定数
    DEP_ACCOUNTING = 0  # 経理
    DEP_SALES = 5  # 営業
    DEP_PRODUCTION = 10  # 製造
    DEP_DEVELOPMENT = 15  # 開発
    DEP_HR = 20  # 人事
    DEP_FIN = 25  # 財務
    DEP_AFFAIRS = 30  # 総務
    DEP_PLANNING = 35  # 企画
    DEP_BUSINESS = 40  # 業務
    DEP_DISTR = 45  # 流通
    DEP_IS = 50  # 情報システム

    # 人
    person = models.ForeignKey('Person')
    # 部署
    department = models.IntegerField()
    # 着任時期
    joined_at = models.DateTimeField()
    # やめた時期
    quited_at = models.DateTimeField(null=True, blank=True)


class Worker(models.Model):

    # 人
    person = models.ForeignKey('Person')
    # 着任時期
    joined_at = models.DateTimeField()
    # やめた時期
    quited_at = models.DateTimeField(null=True, blank=True)
    # 担当上司
    manager = models.ForeignKey('Manager')
