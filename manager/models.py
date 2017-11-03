from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from manager.managers import PersonManager


class Person(AbstractBaseUser):
    objects = PersonManager()

    MAN = 0
    WOMAN = 1

    # 北海道
    HOKKAIDO = 0
    # 東北
    TOHOKU = 10
    AOMORI = 11
    AKITA = 12
    IWATE = 13
    YAMAGATA = 14
    MIYAGI = 15
    HUKUSHIMA = 16
    # 関東
    KANTO = 20
    TOKYO = 21
    CHIBA = 22
    KANAGAWA = 23
    SAITAMA = 24
    TOCHIGI = 25
    IBARAGI = 26
    GUNMA = 27
    # 北陸・中部
    HOKURIKU = 30
    NIIGATA = 31
    NAGANO = 32
    YAMANASHI = 33
    TOYAMA = 34
    ISHIKAWA = 35
    HUKUI = 36
    GIHU = 37
    SHIZUOKA = 38
    AICHI = 39
    # 関西
    KANSAI = 40
    MIE = 41
    SHIGA = 42
    KYOTO = 43
    OSAKA = 44
    HYOGO = 45
    NARA = 46
    WAKAYAMA = 47
    # 中国
    CHUGOKU = 50
    OKAYAMA = 51
    HIROSHIMA = 52
    TOTTORI = 53
    SHIMANE = 54
    YAMAGUCHI = 55
    # 四国
    SHIKOKU = 60
    KAGAWA = 61
    TOKUSHIMA = 62
    EHIME = 63
    KOCHI = 64
    # 九州・沖縄
    KYUSHU = 70
    HUKUOKA = 71
    OITA = 72
    SAGA = 73
    NAGASAKI = 74
    KUMAMOTO = 75
    MIYAZAKI = 76
    KAGOSHIMA = 77
    OKINAWA = 78

    # アカウント名
    identifier = models.CharField(max_length=64, unique=True, blank=False)
    # 名前
    name = models.CharField(max_length=128)
    # メールアドレス
    email = models.EmailField()
    # 誕生日
    birthday = models.DateTimeField()
    # 性別
    sex = models.IntegerField(editable=False)
    # 出身地
    address_from = models.IntegerField()
    # 現住所
    current_address = models.IntegerField()

    # ログイン機能の実装に必要
    is_active = models.BooleanField(default=True)

    # hijack機能の実装に必要
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'identifier'


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
