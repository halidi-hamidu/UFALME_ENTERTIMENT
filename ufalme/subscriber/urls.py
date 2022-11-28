from django.urls import path, include
from . import views
app_name="subscriber"
urlpatterns = [
   path('', views.homePage, name="homePage"),
   path('about-us', views.aboutUs, name="aboutUs"),
   path('entertainments-Plan', views.entertainmentsPlan, name="entertainmentsPlan"),
   path('youtube-package-plan', views.youtubePackage, name="youtubePackage"),
   path('youtube-basic-package-form', views.youTubeBasicPackage, name="youTubeBasicPackage"),
   path('youtube-standard-package-form', views.youTubeStandardPackage, name="youTubeStandardPackage"),
   path('youtube-premium-package-form', views.youTubePremiumPackage, name="youTubePremiumPackage"),
   path('instagram-package-plan', views.instagramPackage, name="instagramPackage"),
   path('instagram-basic-package-form', views.instagramBasicPackage, name="instagramBasicPackage"),
   path('instagram-standard-package-form', views.instagramStandardPackage, name="instagramStandardPackage"),
   path('instagram-premium-package-form', views.instagramPremiumPackage, name="instagramPremiumPackage"),
   path('digital-marketing-distibution', views.digitalMarketingDistribution, name="digitalMarketingDistribution"),
   path('digital-marketing-distibution-basic-package-form', views.digitalMarketingDistributionBasicPackage, name="digitalMarketingDistributionBasicPackage"),
   path('digital-marketing-distibution-standard-package-form', views.digitalMarketingDistributionStandardPackage, name="digitalMarketingDistributionStandardPackage"),
   path('digital-marketing-distibution-premium-package-form', views.digitalMarketingDistributionPremiumPackage, name="digitalMarketingDistributionPremiumPackage"),
   path('earning-money-online-form', views.earningMoneyOnline, name="earningMoneyOnline"),
   path('advertise-bussiness-form', views.advertiseBussiness, name="advertiseBussiness"),
]
