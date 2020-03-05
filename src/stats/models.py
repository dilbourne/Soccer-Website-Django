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

    pl_id = models.OneToOneField(
    PlayerInfo,
    on_delete=models.CASCADE,
    verbose_name="the related attacking player",
    primary_key = True
    )
   
    kwargs = { "null":True, "blank":True }
    last_update = models.DateTimeField(auto_now_add=True)
    appearances = models.IntegerField(**kwargs)
    assists = models.IntegerField(**kwargs)
    big_chances_created = models.IntegerField(**kwargs)
    big_chances_missed = models.IntegerField(**kwargs)
    blocked_shots = models.IntegerField(**kwargs)
    clearances = models.IntegerField(**kwargs)
    crosses = models.IntegerField(**kwargs)
    fouls = models.IntegerField(**kwargs)
    freekicks_scored = models.IntegerField(**kwargs)
    goals = models.IntegerField(**kwargs)
    goals_per_match = models.FloatField(**kwargs)
    goals_with_left_foot = models.IntegerField(**kwargs)
    goals_with_right_foot = models.IntegerField(**kwargs)
    headed_clearance = models.IntegerField(**kwargs)
    headed_goals = models.IntegerField(**kwargs)
    hit_woodwork = models.IntegerField(**kwargs)
    interceptions = models.IntegerField(**kwargs)
    losses = models.IntegerField(**kwargs)
    offsides = models.IntegerField(**kwargs)
    passes = models.IntegerField(**kwargs)
    passes_per_match = models.FloatField(**kwargs)
    penalties_scored = models.IntegerField(**kwargs)
    red_cards = models.IntegerField(**kwargs)
    shooting_accuracy = models.FloatField(**kwargs)
    shots = models.IntegerField(**kwargs)
    shots_on_target = models.IntegerField(**kwargs)
    tackles = models.IntegerField(**kwargs)
    wins = models.IntegerField(**kwargs)
    yellow_cards = models.IntegerField(**kwargs)

    def __str__(self):
        return self.pl_id.name if self.pl_id.name != None else 'Unknown'

class MidfielderStats(models.Model):
    class Meta:
        verbose_name = 'Midfielder Stats'
        verbose_name_plural = 'Midfielder Stats'
    
    pl_id = models.OneToOneField(
    PlayerInfo,
    on_delete=models.CASCADE,
    verbose_name="the related midfielder player",
    primary_key = True
    )
    kwargs = { "null":True, "blank":True }
    last_update = models.DateTimeField(auto_now_add=True)
    # general
    appearances = models.IntegerField(**kwargs)
    losses = models.IntegerField(**kwargs)
    wins = models.IntegerField(**kwargs)
    # team play
    assists = models.IntegerField(**kwargs)
    passes = models.IntegerField(**kwargs)
    passes_per_match = models.FloatField(**kwargs)
    big_chances_created = models.IntegerField(**kwargs)
    crosses = models.IntegerField(**kwargs)
    cross_accuracy = models.FloatField(**kwargs)
    through_balls = models.IntegerField(**kwargs)
    accurate_long_balls = models.IntegerField(**kwargs)
    # discipline
    yellow_cards = models.IntegerField(**kwargs)
    red_cards = models.IntegerField(**kwargs)
    fouls = models.IntegerField(**kwargs)
    offsides = models.IntegerField(**kwargs)
    #attack
    big_chances_missed = models.IntegerField(**kwargs)
    freekicks_scored = models.IntegerField(**kwargs)
    goals = models.IntegerField(**kwargs)
    goals_per_match = models.FloatField(**kwargs)
    goals_with_left_foot = models.IntegerField(**kwargs)
    goals_with_right_foot = models.IntegerField(**kwargs)
    headed_goals = models.IntegerField(**kwargs)
    hit_woodwork = models.IntegerField(**kwargs)
    penalties_scored = models.IntegerField(**kwargs)
    shooting_accuracy = models.FloatField(**kwargs)
    shots = models.IntegerField(**kwargs)
    shots_on_target = models.IntegerField(**kwargs)
    # defence
    tackles = models.IntegerField(**kwargs)
    tackle_success = models.FloatField(**kwargs)
    blocked_shots = models.IntegerField(**kwargs)
    interceptions = models.IntegerField(**kwargs)
    clearances = models.IntegerField(**kwargs)
    headed_clearance = models.IntegerField(**kwargs)
    recoveries = models.IntegerField(**kwargs)
    duels_won = models.IntegerField(**kwargs)
    duels_lost = models.IntegerField(**kwargs)
    successful_50_50 = models.IntegerField(**kwargs)
    aerial_battles_won = models.IntegerField(**kwargs)
    aerial_battles_lost = models.IntegerField(**kwargs)
    errors_leading_to_goal = models.IntegerField(**kwargs)
    def __str__(self):
        return self.pl_id.name if self.pl_id.name != None else 'Unknown'
    
class DefenderStats(models.Model):
    class Meta:
        verbose_name = 'Defender Stats'
        verbose_name_plural = 'Defender Stats'

    pl_id = models.OneToOneField(
    PlayerInfo,
    on_delete=models.CASCADE,
    verbose_name="the related defender",
    primary_key=True
    )
    kwargs = { "null":True, "blank":True }
    last_update = models.DateTimeField(auto_now_add=True)
    # general
    appearances = models.IntegerField(**kwargs)
    wins = models.IntegerField(**kwargs)
    losses = models.IntegerField(**kwargs)
    # defence
    clean_sheets = models.IntegerField(**kwargs)
    goals_conceded = models.IntegerField(**kwargs)
    tackles = models.IntegerField(**kwargs)
    tackle_success = models.IntegerField(**kwargs)
    last_man_tackles = models.IntegerField(**kwargs)
    blocked_shots = models.IntegerField(**kwargs)
    interceptions = models.IntegerField(**kwargs)
    clearances = models.IntegerField(**kwargs)
    headed_clearance = models.IntegerField(**kwargs)
    clearances_off_line = models.IntegerField(**kwargs)
    recoveries = models.IntegerField(**kwargs)
    duels_won = models.IntegerField(**kwargs)
    duels_lost = models.IntegerField(**kwargs)
    successful_50_50 = models.IntegerField(**kwargs)
    aerial_battles_won = models.IntegerField(**kwargs)
    aerial_battles_lost = models.IntegerField(**kwargs)
    own_goals = models.IntegerField(**kwargs)
    errors_leading_to_goal = models.IntegerField(**kwargs)
    # team play
    assists = models.IntegerField(**kwargs)
    passes = models.IntegerField(**kwargs)
    passes_per_match = models.FloatField(**kwargs)
    big_chances_created = models.IntegerField(**kwargs)
    crosses = models.IntegerField(**kwargs)
    cross_accuracy = models.FloatField(**kwargs)
    through_balls = models.IntegerField(**kwargs)
    accurate_long_balls = models.IntegerField(**kwargs)
    # discipline
    yellow_cards = models.IntegerField(**kwargs)
    red_cards = models.IntegerField(**kwargs)
    fouls = models.IntegerField(**kwargs)
    offsides = models.IntegerField(**kwargs)
    # attack
    goals = models.IntegerField(**kwargs)
    headed_goals = models.IntegerField(**kwargs)
    goals_with_right_foot = models.IntegerField(**kwargs)
    goals_with_left_foot = models.IntegerField(**kwargs)
    hit_woodwork = models.IntegerField(**kwargs)
    def __str__(self):
        return self.pl_id.name if self.pl_id.name != None else 'Unknown'

class GoalkeeperStats(models.Model):
    class Meta:
        verbose_name = 'Goalkeeper Stats'
        verbose_name_plural = 'Goalkeeper Stats'
    
    pl_id = models.OneToOneField(
    PlayerInfo,
    on_delete=models.CASCADE,
    verbose_name="the related goalkeeper",
    primary_key = True
    )
    kwargs = { "null":True, "blank":True }
    last_update = models.DateTimeField(auto_now_add=True)
    # general
    appearances = models.IntegerField(**kwargs)
    wins = models.IntegerField(**kwargs)
    losses = models.IntegerField(**kwargs)
    # goalkeeping
    saves = models.IntegerField(**kwargs)
    penalties_saved = models.IntegerField(**kwargs)
    punches = models.IntegerField(**kwargs)
    high_claims = models.IntegerField(**kwargs)
    catches = models.IntegerField(**kwargs)
    sweeper_clearances = models.IntegerField(**kwargs)
    throw_outs = models.IntegerField(**kwargs)
    goal_kicks = models.IntegerField(**kwargs)
    # defence
    clean_sheets = models.IntegerField(**kwargs)
    goals_conceded = models.IntegerField(**kwargs)
    errors_leading_to_goal = models.IntegerField(**kwargs)
    own_goals = models.IntegerField(**kwargs)
    # discipline
    yellow_cards = models.IntegerField(**kwargs)
    red_cards = models.IntegerField(**kwargs)
    fouls = models.IntegerField(**kwargs)
    # team player
    goals = models.IntegerField(**kwargs)
    assists = models.IntegerField(**kwargs)
    passes = models.IntegerField(**kwargs)
    passes_per_match = models.IntegerField(**kwargs)
    accurate_long_balls = models.IntegerField(**kwargs)
    def __str__(self):
        return self.pl_id.name if self.pl_id.name != None else 'Unknown'


   
    
    


