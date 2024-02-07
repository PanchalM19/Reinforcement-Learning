# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

# My understanding:
#"Your setting of the parameter values for each part should have the property that, if your agent followed its optimal policy without being subject to any noise, it would exhibit the given behavior."
# This is given to us!
# Hence, noise in each case will be 0

def question2a():
    """
      Prefer the close exit (+1), risking the cliff (-10).
      Terminal state: (2,2)
      Path should be:
      (0,1)-(1,1)-(2,1)-(2,2)

      EPISODE 1 COMPLETE: RETURN WAS 0.11200000000000002
      AVERAGE RETURNS FROM START STATE: 0.11200000000000002
    """
    answerDiscount = 0.1
    answerNoise = 0
    answerLivingReward = 0.1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2b():
    """
      Prefer the close exit (+1), but avoiding the cliff (-10).
      Terminal state: (2,2)
      Path should be:
      (0,1)-(0,2)-(0,3)-(0,4)-(1,4)-(2,4),(2,3)-(2,2)

      EPISODE 1 COMPLETE: RETURN WAS 0.11111120000000002
      AVERAGE RETURNS FROM START STATE: 0.11111120000000002
    """
    answerDiscount = 0.1
    answerNoise = 0.1
    answerLivingReward = 0.1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2c():
    """
      Prefer the distant exit (+10), risking the cliff (-10).
      Terminal state: (4,2)
      Path should be:
      (0,1)-(1,1)-(2,1)-(3,1)-(4,1)-(4,2)

      EPISODE 1 COMPLETE: RETURN WAS 0.16681
      AVERAGE RETURNS FROM START STATE: 0.16681

    """
    answerDiscount = 0.3
    answerNoise = 0
    answerLivingReward = 0.1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2d():
    """
      Prefer the distant exit (+10), avoiding the cliff (-10).
      Terminal state: (4,2)
      Path should be:
      (0,1)-(0,2)-(0,3)-(0,4)-(1,4)-(2,4),(3,4)-(4,4)-(4,3)-(4,2)

      EPISODE 1 COMPLETE: RETURN WAS 0.285905492
      AVERAGE RETURNS FROM START STATE: 0.285905492
    """
    answerDiscount = 0.3
    answerNoise = 0.1
    answerLivingReward = 0.2
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question2e():
    """
      Avoid both exits and the cliff (so an episode should never terminate).

      Agent got stuck at (0,4)
    """
    answerDiscount = 0.9 #It should be less than 1
    answerNoise = 0
    answerLivingReward = 1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
