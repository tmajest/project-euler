set nocompatible
source $VIMRUNTIME/vimrc_example.vim
source $VIMRUNTIME/mswin.vim
behave mswin

if has("gui_running")
  " GUI is running or is about to start.
  " Maximize gvim window.
  set lines=60 columns=110
else
  " This is console Vim.
  if exists("+lines")
    set lines=60
  endif
  if exists("+columns")
    set columns=110
  endif
endif

winpos 0 0

let g:NERDTreeWinPos = "left"
nnoremap <c-N> :NERDTreeToggle<cr>

colorscheme codeschool
set guioptions-=T " Removes top toolbar
set guioptions-=r " Removes right hand scroll bar
set go-=L " Removes left hand scroll bar

nnoremap <a-j> 4jzz
nnoremap <a-k> 4kzz
vnoremap <a-j> 4jzz
vnoremap <a-k> 4kzz

set expandtab
set shiftwidth=4
set softtabstop=4

set guifont=Consolas
set fileformats=dos
set number

set ignorecase
set splitright
set splitbelow
set iskeyword+=-
set iskeyword+=_

set backupdir=C:\backup
set directory=C:\backup
let $TMP="c:/backup"

set diffexpr=MyDiff()
function MyDiff()
  let opt = '-a --binary '
  if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif
  if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif
  let arg1 = v:fname_in
  if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif
  let arg2 = v:fname_new
  if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif
  let arg3 = v:fname_out
  if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif
  let eq = ''
  if $VIMRUNTIME =~ ' '
    if &sh =~ '\<cmd'
      let cmd = '""' . $VIMRUNTIME . '\diff"'
      let eq = '"'
    else
      let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'
    endif
  else
    let cmd = $VIMRUNTIME . '\diff'
  endif
  silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3 . eq
endfunction

