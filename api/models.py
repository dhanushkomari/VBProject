from django.db import models

# Create your models here.


####################################################################
#####################   VOICE API MODEL    #########################        
####################################################################

class Voice(models.Model):
    bot_id = models.CharField(max_length=500)
    file = models.FileField(upload_to='file_uploads', blank=True, null=True)
    speech_to_text = models.TextField()
    type = models.CharField(max_length = 30)
    output = models.TextField()
    language = models.CharField(max_length = 30, blank=True, null=True)
    time = models.DecimalField(max_digits=30, decimal_places=6)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Voice'
        verbose_name_plural = 'Voices'
    
    def __str__(self):
        return str(self.bot_id)

####################################################################
###################   VERSION SETTINGS MODEL     ###################    
####################################################################
    

class VersionSetting(models.Model):
    version_name = models.CharField(max_length = 30)
    git_command = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Version Setting'
        verbose_name_plural = 'Version Settings'
        
    def __str__(self):
        return str(self.version_name)


class FlatVersionSettings(models.Model):
    version_name = models.CharField(max_length =30, help_text = 'enter version of the Flat weights')
    git_command = models.CharField(max_length = 300, help_text = 'enter the git link here')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Version Flat Setting'
        verbose_name_plural = 'Version Flat Settings'

    def __str__(self):
        return str(self.version_name)
