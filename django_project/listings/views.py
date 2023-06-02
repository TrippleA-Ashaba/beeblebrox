from django.shortcuts import render

# Create your views here.


def home(request):
    listings = [
        {
            "title": "Senior Ruby on Rails Developer: Fully Remote",
            "company": "Proxify AB",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/proxify-ab",
                "https://weworkremotely.com/remote-jobs/proxify-ab-senior-ruby-on-rails-developer-fully-remote",
            ],
        },
        {
            "title": "Integrations Team Lead",
            "company": "CoinLedger",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/coinledger",
                "https://weworkremotely.com/remote-jobs/coinledger-integrations-team-lead",
            ],
        },
        {
            "title": "Senior Ruby on Rails - (USD $80-100k starting salary)",
            "company": "QuickMail",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/quickmail",
                "https://weworkremotely.com/remote-jobs/quickmail-senior-ruby-on-rails-usd-80-100k-starting-salary",
            ],
        },
        {
            "title": "Software Developer",
            "company": "Hashlist",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/hashlist",
                "https://weworkremotely.com/remote-jobs/hashlist-software-developer",
            ],
        },
        {
            "title": "Software Engineer (Backend)",
            "company": "Sticker Mule",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/sticker-mule",
                "https://weworkremotely.com/remote-jobs/sticker-mule-software-engineer-backend",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
        {
            "title": "Senior PHP Web Developers– Cyprus, Greece or Remote",
            "company": "XM",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/xm",
                "https://weworkremotely.com/remote-jobs/xm-senior-php-web-developers-cyprus-greece-or-remote-1",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
        {
            "title": "Site Reliability Engineer",
            "company": "Sticker Mule",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/sticker-mule",
                "https://weworkremotely.com/remote-jobs/sticker-mule-site-reliability-engineer-1",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
        {
            "title": "Ruby in Rails Engineer ",
            "company": "Whitespectre",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/whitespectre",
                "https://weworkremotely.com/remote-jobs/whitespectre-ruby-in-rails-engineer",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
        {
            "title": "Senior WHMSC Web Developer Lead",
            "company": "RapidSeedbox Ltd",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/rapidseedbox-ltd",
                "https://weworkremotely.com/remote-jobs/rapidseedbox-ltd-senior-whmsc-web-developer-lead",
            ],
        },
        {
            "title": "Senior Software Engineer",
            "company": "Paymentology",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/paymentology",
                "https://weworkremotely.com/remote-jobs/paymentology-senior-software-engineer-1",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
        {
            "title": "Principal Ruby on Rails Developer",
            "company": "Lifetimely",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/lifetimely",
                "https://weworkremotely.com/remote-jobs/lifetimely-principal-ruby-on-rails-developer",
            ],
        },
        {
            "title": "Lead Full-Stack PHP Developer",
            "company": "BBE Marketing Inc",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/bbe-marketing-inc",
                "https://weworkremotely.com/remote-jobs/bbe-marketing-inc-lead-full-stack-php-developer",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
        {
            "title": "Full-Stack Wordpress Developer",
            "company": "BBE Marketing Inc",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/bbe-marketing-inc",
                "https://weworkremotely.com/remote-jobs/bbe-marketing-inc-full-stack-wordpress-developer-4",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
        {
            "title": "Senior Rails Developer",
            "company": "Simplero",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/simplero",
                "https://weworkremotely.com/remote-jobs/simplero-senior-rails-developer-2",
            ],
        },
        {
            "title": "Flexible Web Developer for AI-driven Startup Studio",
            "company": "Method Labs LLC",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/method-labs-llc",
                "https://weworkremotely.com/remote-jobs/method-labs-llc-flexible-web-developer-for-ai-driven-startup-studio",
            ],
        },
        {
            "title": "Full-Stack Ruby on Rails Developer",
            "company": "DesignFiles",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/designfiles",
                "https://weworkremotely.com/remote-jobs/designfiles-full-stack-ruby-on-rails-developer",
            ],
        },
        {
            "title": "Senior QA Engineer",
            "company": "TestGorilla",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/testgorilla",
                "https://weworkremotely.com/remote-jobs/testgorilla-senior-qa-engineer-1",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
        {
            "title": "Senior Open Source Developer & DevOps (Python, Django, React, AWS/OpenStack)",
            "company": "OpenCraft",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/opencraft",
                "https://weworkremotely.com/remote-jobs/opencraft-senior-open-source-developer-devops-python-django-react-aws-openstack",
            ],
        },
        {
            "title": "Senior Fullstack Engineer (Ruby/Rails)",
            "company": "TimeZest",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/timezest",
                "https://weworkremotely.com/remote-jobs/timezest-senior-fullstack-engineer-ruby-rails-1",
            ],
        },
        {
            "title": "Lead Android or/and Iphone Engineer",
            "company": "ttt246 llc",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/ttt246-llc",
                "https://weworkremotely.com/remote-jobs/ttt246-llc-lead-android-or-and-iphone-engineer",
            ],
        },
        {
            "title": "Senior Symfony PHP Full Stack Developer - Remote & Full Time",
            "company": "Internet Projects Ltd",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/internet-projects-ltd",
                "https://weworkremotely.com/remote-jobs/internet-projects-ltd-senior-symfony-php-full-stack-developer-remote-full-time-1",
            ],
        },
        {
            "title": "Full Stack Web Developer - WordPress & More ",
            "company": "Yoko Co",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/yoko-co",
                "https://weworkremotely.com/remote-jobs/yoko-co-full-stack-web-developer-wordpress-more",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
        {
            "title": "Remote Senior Odoo Developer (m/f/d)",
            "company": "much",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/much",
                "https://weworkremotely.com/remote-jobs/much-remote-senior-odoo-developer-m-f-d",
            ],
        },
        {
            "title": "Rails Lead Engineer for amazing education / community platform",
            "company": "Institute of OM",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/institute-of-om",
                "https://weworkremotely.com/remote-jobs/institute-of-om-rails-lead-engineer-for-amazing-education-community-platform",
            ],
        },
        {
            "title": "Full Stack Engineer",
            "company": "OCR Labs",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/ocr-labs",
                "https://weworkremotely.com/remote-jobs/ocr-labs-full-stack-engineer-2",
            ],
        },
        {
            "title": "AI engineer",
            "company": "Sticker Mule",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/sticker-mule",
                "https://weworkremotely.com/remote-jobs/sticker-mule-ai-engineer-1",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
        {
            "title": "JavaScript Developer (React or Vue or Angular, with Node.js)",
            "company": "RemoteMore",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/remotemore",
                "https://weworkremotely.com/remote-jobs/remotemore-javascript-developer-react-or-vue-or-angular-with-node-js-3",
            ],
        },
        {
            "title": "Senior Full Stack Developer",
            "company": "Bottomless",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/bottomless",
                "https://weworkremotely.com/remote-jobs/bottomless-senior-full-stack-developer-9",
            ],
        },
        {
            "title": "Senior Independent Software Developer ($110-$190/hr)",
            "company": "A.Team",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/a-team",
                "https://weworkremotely.com/remote-jobs/a-team-senior-independent-software-developer-110-190-hr",
            ],
        },
        {
            "title": "Software engineer (Frontend)",
            "company": "Sticker Mule",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/sticker-mule",
                "https://weworkremotely.com/remote-jobs/sticker-mule-software-engineer-frontend",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
        {
            "title": "Fullstack Developer (Phoenix LiveView / Elixir)",
            "company": "InspireHQ",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/inspirehq",
                "https://weworkremotely.com/remote-jobs/inspirehq-fullstack-developer-phoenix-liveview-elixir",
            ],
        },
        {
            "title": "Full Stack Software Engineer",
            "company": "QuickTrials",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/quicktrials",
                "https://weworkremotely.com/remote-jobs/quicktrials-full-stack-software-engineer",
            ],
        },
        {
            "title": "Freelance QA Engineer at Dusseau and Company, LLC",
            "company": "Contra",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/contra",
                "https://weworkremotely.com/remote-jobs/contra-freelance-qa-engineer-at-dusseau-and-company-llc",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
        {
            "title": "WordPress Developer",
            "company": "Awesome Motive",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/awesome-motive",
                "https://weworkremotely.com/remote-jobs/awesome-motive-wordpress-developer-1",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
        {
            "title": "Embedded Linux Developer (all genders welcome) Remote in Europe",
            "company": "Proemion",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/proemion",
                "https://weworkremotely.com/remote-jobs/proemion-embedded-linux-developer-all-genders-welcome-remote-in-europe",
            ],
        },
        {
            "title": "Senior Shopify Developer (Remote + Flexible)",
            "company": "Storetasker",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/storetasker",
                "https://weworkremotely.com/remote-jobs/storetasker-senior-shopify-developer-remote-flexible-1",
            ],
        },
        {
            "title": "WordPress Developer",
            "company": "aThemes",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/athemes",
                "https://weworkremotely.com/remote-jobs/athemes-wordpress-developer-2",
            ],
        },
        {
            "title": "Software engineer",
            "company": "Stimulus",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/stimulus",
                "https://weworkremotely.com/remote-jobs/stimulus-software-engineer",
            ],
        },
        {
            "title": "Full Stack Engineer",
            "company": "Frost",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/frost",
                "https://weworkremotely.com/remote-jobs/frost-full-stack-engineer",
            ],
        },
        {
            "title": "Application Developer | C++, Qt, QML, Fullstack Engineer - Transforming Creative Writing",
            "company": "R.O.M. logicware GmbH",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/r-o-m-logicware-gmbh",
                "https://weworkremotely.com/remote-jobs/r-o-m-logicware-gmbh-application-developer-c-qt-qml-fullstack-engineer-transforming-creative-writing",
            ],
        },
        {
            "title": "Mentor - Software Engineering Career Track (Part-time/Remote)",
            "company": "Springboard",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/springboard",
                "https://weworkremotely.com/remote-jobs/springboard-mentor-software-engineering-career-track-part-time-remote-3",
            ],
        },
        {
            "title": "Software Engineer - Golang",
            "company": "Threecolts",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/threecolts",
                "https://weworkremotely.com/remote-jobs/threecolts-software-engineer-golang",
            ],
        },
        {
            "title": "Staff Engineer",
            "company": "LeadSimple, Inc.",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/leadsimple-inc",
                "https://weworkremotely.com/remote-jobs/leadsimple-inc-staff-engineer",
            ],
        },
        {
            "title": "PHP Developer",
            "company": "OperateBeyond",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/operatebeyond",
                "https://weworkremotely.com/remote-jobs/operatebeyond-php-developer",
            ],
        },
        {
            "title": "Intermediate or Senior Full Stack Developer (PHP/Laravel/Vue.js)",
            "company": "Batch",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/batch",
                "https://weworkremotely.com/remote-jobs/batch-intermediate-or-senior-full-stack-developer-php-laravel-vue-js",
            ],
        },
        {
            "title": "Senior Frontend Engineer (Angular)",
            "company": "TestGorilla",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/testgorilla",
                "https://weworkremotely.com/remote-jobs/testgorilla-senior-frontend-engineer-angular-3",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
        {
            "title": "Frontend Engineer - Marketing",
            "company": "Adblock, Inc.",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/adblock-inc",
                "https://weworkremotely.com/remote-jobs/adblock-inc-frontend-engineer-marketing",
            ],
        },
        {
            "title": "Freelance Front End Development",
            "company": "Contra",
            "region": "Anywhere in the World",
            "urls": [
                "https://weworkremotely.com/company/contra",
                "https://weworkremotely.com/remote-jobs/contra-freelance-front-end-development",
                "https://weworkremotely.com/top-remote-companies",
            ],
        },
    ]

    return render(request, "home.html", {"listings": listings})
