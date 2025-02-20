from flask_ask import audio, statement, question
from flask import request
from plexmusicplayer import ask, queue


# --------------------------------------------------------------------------------------------
# Amazon Playback - Intents
@ask.launch
def new_ask():
    welcome = "Benvenuto sul tuo Plex Music Player. Cosa vuoi sentire?"
    reprompt = "Temo di non aver capito. Potresti ripetere per favore?"
    return question(welcome) \
        .reprompt(reprompt)


@ask.on_playback_started()
def started(offset):
    offset /= 1000
    print("Playback started at %s" % offset)


@ask.on_playback_stopped()
def stopped(offset):
    offset /= 1000
    print("Playback stopped at %s" % offset)
    queue.current.set_offset(offset)


@ask.on_playback_nearly_finished()
def nearly_finished():
    next = queue.whats_next
    if next:
        return audio().enqueue(next.stream_url)


@ask.on_playback_finished()
def play_back_finished():
    if queue.whats_next:
        queue.go_next()


@ask.intent('AMAZON.NextIntent')
def next_song():
    if queue.whats_next:
        return audio("").play(queue.go_next().stream_url)
    else:
        return audio("Mi spiace, qualcosa non ha funzionato selezionando la canzone succesiva.").stop()


@ask.intent('AMAZON.PreviousIntent')
def previous_song():
    if queue.whats_prev:
        return audio("").play(queue.go_prev().stream_url)
    else:
        return audio("Mi spiace, qualcosa non ha funzionato selezionando la conzone precedente.").stop()


@ask.intent('AMAZON.StartOverIntent')
def restart_track():
    if queue.current:
        return audio("").play(queue.current.stream_url, offset=0)


@ask.intent('AMAZON.PauseIntent')
def pause():
    return audio("").stop()


@ask.intent('AMAZON.ResumeIntent')
def resume():
    return audio("").resume()


@ask.intent('AMAZON.ShuffleOnIntent')
def shuffle():
    queue.shuffle()
    return statement("Playlist shuffled")


@ask.intent('AMAZON.StopIntent')
def stop():
    return audio('Goodbye').clear_queue(stop=True)


@ask.session_ended
def session_ended():
    return "", 200
