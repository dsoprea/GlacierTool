Introduction
============

This is a tool to allow you to quickly push massive archives into Glacier, an ultra low-cost storage solution. It's fast to upload and cheap to maintain (currently $10 per terabyte/month), but there's a four-hour delay in all retrieval requests and a finite window to download.


Notes
=====

- This project is meant for large uploads. It doesn't do small-uploads (the mechanism Currently, this project only provides the mechanism to upload quickly. I couldn't find another reliable, current tool to do large uploads, so I wrote one. I'll write a download-tool in the near future. Until then, use what's already out there or request one via an issue.

- The Amazon library (`boto <https://github.com/boto/boto>`_) that many/most people use to access AWS services (including Glacier) is currently broken for multipart uploads and the version that seems to work fine for multipart uploads is broken for Python 3. So, this library uses *boto* version 2.29.1 under Python 2.7 .


Usage
=====

The command is fully-documented at the command-line. Just provide the "-h" parameter to print the usage::

    $ gt_upload_large -h
    usage: gt_upload_large [-h] [-em ESTIMATED_MBPS] [-pt PART_SIZE]
                           vault_name filepath description

    Push a large archive into long-term storage.

    positional arguments:
      vault_name            Vault name
      filepath              File-path to upload
      description           Description of uploaded file

    optional arguments:
      -h, --help            show this help message and exit
      -em ESTIMATED_MBPS, --estimated-mbps ESTIMATED_MBPS
                            Mbps to estimate a duration against
      -pt PART_SIZE, --part-size PART_SIZE
                            Part-size in bytes. Defaults to 4M. Must be between 1M
                            and 4G.


To perform the upload, you'll have to define the AWS access- and secret-key in the environment::

    $ export AWS_ACCESS_KEY=XXX
    $ export AWS_SECRET_KEY=YYY

    $ gt_upload_large image-backups /mnt/tower/backups/images-main-2010-20150617-2211.tar.xz images-main-2010-20150617-2211.tar.xz -em 11.33
    Uploading: [/mnt/array/backups/images-main-2010-20150617-2211.tar.xz]
    Size: (15.78) G
    Start time: [2015-07-05 01:22:01]
    Estimated duration: (3.17) hours => [2015-07-05 04:32:11] @ (11.33) Mbps
    Archive ID: [IEGZ8uXToCDIgO3pMrrIHBIcJs...YyNlPigEwIR2NA]
    Duration: (3.16) hours @ (11.37) Mbps

    $ gt_upload_large image-backups /mnt/tower/backups/images-main-2011-20150617-2211.tar.xz images-main-2011-20150617-2211.tar.xz -em 11.37
    Uploading: [/mnt/array/backups/images-main-2011-20150617-2211.tar.xz]
    Size: (26.66) G
    Start time: [2015-07-05 10:07:58]
    Estimated duration: (5.33) hours => [2015-07-05 15:28:03] @ (11.37) Mbps

Notice that the output tells you the actual rate of the upload (the *boto* call that I use doesn't provide a progress callback with which to provide realtime feedback). You can pass this value into the command for the next upload with the "-em" parameter to estimate the time-until-completion.

It's probably best to record the archive-IDs somewhere. It'll take you four-hours for an inventory request to be fulfilled (to get a list of your archives) and Amazon only uploads its inventory of your archives every twenty-four hours (so you won't even be able to get a list the first day).
