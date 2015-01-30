#!/bin/bash

awk '
BEGIN{lowercase="[a-z]"}
{

# filters out blank titles
if (NF != 4){
    next;
}


# filters out everything except "en "
# space is for filtering out extensions
if (substr($0,1,3)!="en "){next;}

# filters out special pages
if ((substr($2,1,6)=="Media:")||\
    (substr($2,1,8)=="Special:")||\
    (substr($2,1,5)=="Talk:")||\
    (substr($2,1,5)=="User:")||\
    (substr($2,1,10)=="User_talk:")||\
    (substr($2,1,8)=="Project:")||\
    (substr($2,1,13)=="Project_talk:")||\
    (substr($2,1,5)=="File:")||\
    (substr($2,1,10)=="File_talk:")||\
    (substr($2,1,10)=="MediaWiki:")||\
    (substr($2,1,15)=="MediaWiki_talk:")||\
    (substr($2,1,9)=="Template:")||\
    (substr($2,1,14)=="Template_talk:")||\
    (substr($2,1,5)=="Help:")||\
    (substr($2,1,10)=="Help_talk:")||\
    (substr($2,1,9)=="Category:")||\
    (substr($2,1,14)=="Category_talk:")||\
    (substr($2,1,7)=="Portal:")||\
    (substr($2,1,10)=="Wikipedia:")||\
    (substr($2,1,15)=="Wikipedia_talk:")){next;}

# filters out lowercase titles
if (match(substr($2,1,1),lowercase)){ next; }

# filters out the following files
if ((substr($2,length($2)-3,4)==".jpg")||\
    (substr($2,length($2)-3,4)==".gif")||\
    (substr($2,length($2)-3,4)==".png")||\
    (substr($2,length($2)-3,4)==".JPG")||\
    (substr($2,length($2)-3,4)==".GIF")||\
    (substr($2,length($2)-3,4)==".PNG")||\
    (substr($2,length($2)-3,4)==".txt")||\
    (substr($2,length($2)-3,4)==".ico")){next;}

# filters out boiler plates
if (($2 == "404_error/")||\
    ($2 == "Main_Page")||\
    ($2 == "Hypertext_Transfer_Protocol")||\
    ($2 == "Search")){next;}

# prints everything else
printf("%s\t%s\n",$2,$3);
}
'