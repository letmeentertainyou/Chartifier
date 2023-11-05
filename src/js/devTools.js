/*
These tools will not be included in the JS bundler but they are nice for dev work.
*/

'use strict'

/* UTILITY */

const echo     = message   => document.write(message)
const nl       = _         => document.write('<br>')
const reset    = _         => document.body.innerHTML = ''
