;Browser_Home
^Browser_Home::
    SendInput, {Media_Play_Pause}
    Return

$Browser_Home::Send {Media_Play_Pause}

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


;Launch_Mail
^Launch_Mail::
    SendInput, {Launch_Mail}
    Return

$Launch_Mail::Send {Media_Prev}


;Browser_Stop
^Browser_Stop::
    SendInput, {Browser_Stop}
    Return

$Browser_Stop::Send {Media_Stop}




;Browser_Refresh
^Browser_Refresh::
    SendInput, {Browser_Refresh}
    Return

$Browser_Refresh::Send {Media_Next}


;Browser_Search
^Browser_Search::
    SendInput, {Browser_Search}
    Return

$Browser_Search::Send {Volume_Mute}


;%appdata% -> Microsoft -> Windows -> Menu Inicio -> Programas -> Inicio -> PEGAR ACCESO DIRECTO AQUI


Browser_Favorites::
Sleep::




;Browser_Home
;Browser_Back
;Browser_Forward
;Browser_Refresh
;Browser_Stop
;Launch_Mail
;Browser_Search
;Browser_Favorites
;Sleep
