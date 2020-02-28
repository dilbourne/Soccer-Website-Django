from django.db import models

# Create your models here.
class PlayerInfo(models.Model):
    class Meta:
        verbose_name = 'Player Information'
        verbose_name_plural = 'Player Information'
    role_choices = (
        ('F','Forward'),
        ('M','Midfielder'),
        ('D','Defender'),
        ('G','Goalkeeper')
    )
    pl_id = models.IntegerField(primary_key=True)
    club = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    dob = models.DateField()
    name = models.CharField(max_length=40)
    shirt_num = models.IntegerField()
    role = models.CharField(max_length=1,choices=role_choices)

    def __str__(self):
        return self.name

class PlayerStats(models.Model):
    class Meta:
        verbose_name = 'Player Statistics'
        verbose_name_plural = 'Player Statistics'
    pl_id = models.ForeignKey(
        PlayerInfo,
        on_delete=models.CASCADE,
        verbose_name="the related player"
        )
    last_update = models.DateTimeField(auto_now_add=True)
    appearances = models.IntegerField()
    assists = models.IntegerField()
    big_chances_created = models.IntegerField()
    big_chances_missed = models.IntegerField()
    blocked_shots = models.IntegerField()
    clearances = models.IntegerField()
    crosses = models.IntegerField()
    fouls = models.IntegerField()
    freekicks_scored = models.IntegerField()
    goals = models.IntegerField()
    goals_per_match = models.FloatField()
    goals_with_left_foot = models.IntegerField()
    goals_with_right_foot = models.IntegerField()
    headed_clearance = models.IntegerField()
    headed_goals = models.IntegerField()
    hit_woodwork = models.IntegerField()
    intercetions = models.IntegerField()
    losses = models.IntegerField()
    offsides = models.IntegerField()
    passes = models.IntegerField()
    passes_per_match = models.FloatField()
    penalties_scored = models.IntegerField()
    red_cards = models.IntegerField()
    shooting_accuracy = models.FloatField()
    shots = models.IntegerField()
    shots_on_target = models.IntegerField()
    tackles = models.IntegerField()
    wins = models.IntegerField()
    yellow_cards = models.IntegerField()





