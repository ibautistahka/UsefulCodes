;F10
^F10::
    SendInput, {F10}
    Return

$F10::Send {Volume_Mute}

;Browser_Back
^Browser_Back::
    SendInput, {Browser_Back}
    Return

$Browser_Back::Send {Volume_Down 5}

;Browser_Forward
^Browser_Forward::
    SendInput, {Browser_Forward}
    Return

$Browser_Forward::Send {Volume_Up 5}


;Browser_Home
;Browser_Back
;Browser_Forward
;Browser_Refresh
;Browser_Stop
;Launch_Mail
;Browser_Search
;Browser_Favorites
;Sleep
