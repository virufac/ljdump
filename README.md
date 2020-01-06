
## ljdump with xmlread - output LJ archives to template html
### (by fork maintainer)

When many other LJ archiving tools went proprietary or were shut down by rate limiting, this tool stood the test of time and still works to this day as far as I know. It's been less than a year since I've used it, I think.

Since using this tool from my youth and learning to program a bit, I've come to address a few of its problems... At least the ones that I had.

Shitty XML files -- not the author's fault. XML files are innately trash. :P.
Unreliable encoding. Reliance on Wordpress to fix it. I say this with the greatest respect. This tool is efficient and merely need something like this template builder.

You can transform xml to html with a simple template like posttemp.html. See the screencaps directory.

In that template file, you can see that I'm using some bootstrap classes in my post. But they're not important. `$TIME`, `$DATE`, `$POST` -- these are the placeholders that insert the data from the xml.

I hate to say it but for all the xml data has on it, those were the only things I found worth salvaging.

When its finished outputting every html template (to be again, templated into a CSS design or something) it will dump the entire journal as a single json file as well, which is so much better for me at least...

#### in pace requiescat, livejournal.


--

(BTW if you are looking for support trying to use this tool and are not having luck contacting the original programmer, let me know. My python2 is not the best but I can probably figure it out. I deleted my LJs a while back when the Russian Oh No They Didn't invasion was complete. )

=================================

## ljdump - livejournal archiver
### (by original coder at the the original repo)

This program reads the journal entries from a livejournal (or compatible)
blog site and archives them in a subdirectory named after the journal name.

The simplest way to run this is to execute the ljdump.py script with Python.
Depending on your OS, you may be able to double-click the ljdump.py script
directly, or you may need to open a Terminal/Command Prompt window to run it.
Either way, it will prompt you for your Livejournal username and password,
then download all your journal entries, comments, and userpics.

You may optionally download entries from a different journal (a community)
where you are a member. If you are a community maintainer, you can also
download comments from the community.

If you want to save your username and password so you don't have to type
it every time you run ljdump, you can save it in the configuration file.

The configuration is read from "ljdump.config". A sample configuration is
provided in "ljdump.config.sample", which should be copied and then edited.
The configuration settings are:

  server - The XMLRPC server URL. This should only need to be changed
           if you are dumping a journal that is livejournal-compatible
           but is not livejournal itself.

  username - The livejournal user name. A subdirectory will be created
             with this same name to store the journal entries.

  password - The account password. This password is never sent in the
             clear; the livejournal "challenge" password mechanism is used.

  journal - Optional: The journal to download entries from. If this is
            not specified, the "username" journal is downloaded. If this
            is specified, then only the named journals will be downloaded
            (this element may be specified more than once to download
            multiple journals).

This program may be run as often as needed to bring the backup copy up
to date. Both new and updated items are downloaded.

The community http://ljdump.livejournal.com has been set up for questions
or comments.

-----

convertdump - convert ljdump format to wordpress importer format
Contributed by Sean M. Graham (www.sean-graham.com) and others

This will convert a pydump archive into something compatible with the
WordPress LiveJournal importer.  This is the same format used by the Windows
ljArchive exporter.

Arguments:
    -u  --user      username of archive to process [required]
    -l  --limit     limit the number of entries in each xml file (default 250)
    -i  --insecure  include private and protected entries in the output
    -h  --help      show this help page

Example:
    ./convertdump.py --user stevemartin --limit 200 --insecure
