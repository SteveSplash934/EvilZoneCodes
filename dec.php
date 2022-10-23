<?php

$myHash = '$2a$10$VO4OOc2nt7xdiL02F3NAZekleAgB6B/CFkHtb8gOIOuW9dnztp77W';

if (password_verify('EvilZone', $myHash)) {
    echo 'Password is valid!';
} else {
    echo 'Invalid password.';
}

?>
