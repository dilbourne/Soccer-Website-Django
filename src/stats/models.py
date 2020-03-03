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
    name = models.CharField(max_length=40,unique=True)
    shirt_num = models.IntegerField()
    role = models.CharField(max_length=1,choices=role_choices)

    def __str__(self):
        return self.name

class ForwardStats(models.Model):
    class Meta:
        verbose_name = 'Forward Stats'
        verbose_name_plural = 'Forward Stats'

    pl_id = models.ForeignKey(
    PlayerInfo,
    on_delete=models.CASCADE,
    verbose_name="the related attacking player"
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
    interceptions = models.IntegerField()
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

class MidfielderStats(models.Model):
    class Meta:
        verbose_name = 'Midfielder Stats'
        verbose_name_plural = 'Midfielder Stats'
    
    pl_id = models.ForeignKey(
    PlayerInfo,
    on_delete=models.CASCADE,
    verbose_name="the related midfielder player"
    )
    last_update = models.DateTimeField(auto_now_add=True)
    # general
    appearances = models.IntegerField()
    losses = models.IntegerField()
    wins = models.IntegerField()
    # team play
    assists = models.IntegerField()
    passes = models.IntegerField()
    passes_per_match = models.FloatField()
    big_chances_created = models.IntegerField()
    crosses = models.IntegerField()
    cross_accuracy = models.FloatField()
    through_balls = models.IntegerField()
    accurate_long_balls = models.IntegerField()
    # discipline
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    fouls = models.IntegerField()
    offsides = models.IntegerField()
    #attack
    big_chances_missed = models.IntegerField()
    freekicks_scored = models.IntegerField()
    goals = models.IntegerField()
    goals_per_match = models.FloatField()
    goals_with_left_foot = models.IntegerField()
    goals_with_right_foot = models.IntegerField()
    headed_goals = models.IntegerField()
    hit_woodwork = models.IntegerField()
    penalties_scored = models.IntegerField()
    shooting_accuracy = models.FloatField()
    shots = models.IntegerField()
    shots_on_target = models.IntegerField()
    # defence
    tackles = models.IntegerField()
    tackle_success = models.FloatField()
    blocked_shots = models.IntegerField()
    interceptions = models.IntegerField()
    clearances = models.IntegerField()
    headed_clearance = models.IntegerField()
    recoveries = models.IntegerField()
    duels_won = models.IntegerField()
    duels_lost = models.IntegerField()
    successful_50_50 = models.IntegerField()
    aerial_battles_won = models.IntegerField()
    aerial_battles_lost = models.IntegerField()
    errors_leading_to_goal = models.IntegerField()
    
class DefenderStats(models.Model):
    class Meta:
        verbose_name = 'Defender Stats'
        verbose_name_plural = 'Defender Stats'

    pl_id = models.ForeignKey(
    PlayerInfo,
    on_delete=models.CASCADE,
    verbose_name="the related defender"
    )
    last_update = models.DateTimeField(auto_now_add=True)
    # general
    appearances = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    # defence
    clean_sheets = models.IntegerField()
    goals_conceded = models.IntegerField()
    tackles = models.IntegerField()
    tackle_success = models.IntegerField()
    last_man_tackles = models.IntegerField()
    blocked_shots = models.IntegerField()
    interceptions = models.IntegerField()
    clearances = models.IntegerField()
    headed_clearance = models.IntegerField()
    clearances_off_line = models.IntegerField()
    recoveries = models.IntegerField()
    duels_won = models.IntegerField()
    duels_lost = models.IntegerField()
    successful_50_50 = models.IntegerField()
    aerial_battles_won = models.IntegerField()
    aerial_battles_lost = models.IntegerField()
    own_goals = models.IntegerField()
    errors_leading_to_goal = models.IntegerField()
    # team play
    assists = models.IntegerField()
    passes = models.IntegerField()
    passes_per_match = models.FloatField()
    big_chances_created = models.IntegerField()
    crosses = models.IntegerField()
    cross_accuracy = models.FloatField()
    through_balls = models.IntegerField()
    accurate_long_balls = models.IntegerField()
    # discipline
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    fouls = models.IntegerField()
    offsides = models.IntegerField()
    # attack
    goals = models.IntegerField()
    headed_goals = models.IntegerField()
    goals_with_right_foot = models.IntegerField()
    goals_with_left_foot = models.IntegerField()
    hit_woodwork = models.IntegerField()


class GoalkeeperStats(models.Model):
    class Meta:
        verbose_name = 'Goalkeeper Stats'
        verbose_name_plural = 'Goalkeeper Stats'
    
    pl_id = models.ForeignKey(
    PlayerInfo,
    on_delete=models.CASCADE,
    verbose_name="the related goalkeeper"
    )
    last_update = models.DateTimeField(auto_now_add=True)
    # general
    appearances = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    # goalkeeping
    saves = models.IntegerField()
    penalties_saved = models.IntegerField()
    punches = models.IntegerField()
    high_claims = models.IntegerField()
    catches = models.IntegerField()
    sweeper_clearances = models.IntegerField()
    throw_outs = models.IntegerField()
    goal_kicks = models.IntegerField()
    # defence
    clean_sheets = models.IntegerField()
    goals_conceded = models.IntegerField()
    errors_leading_to_goal = models.IntegerField()
    own_goals = models.IntegerField()
    # discipline
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    fouls = models.IntegerField()
    # team player
    goals = models.IntegerField()
    assists = models.IntegerField()
    passes = models.IntegerField()
    passes_per_match = models.IntegerField()
    accurate_long_balls = models.IntegerField()



   
    
    


