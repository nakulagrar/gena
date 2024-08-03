from flask import Flask, jsonify,request
import os

app = Flask(__name__)

@app.route('/employee_details', methods=['GET'])
def get_data():
    data = [
    {
        "Bonus %": "14.009",
        "First Name": "null",
        "Gender": "null",
        "Last Login Time": "8:29 AM",
        "Salary": 41126,
        "Senior Management": "null",
        "Start Date": "Sat, 17 Dec 2011 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "6.185",
        "First Name": "null",
        "Gender": "null",
        "Last Login Time": "6:59 PM",
        "Salary": 40297,
        "Senior Management": "null",
        "Start Date": "Tue, 18 Sep 2007 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "10.391",
        "First Name": "null",
        "Gender": "null",
        "Last Login Time": "3:01 AM",
        "Salary": 113732,
        "Senior Management": "null",
        "Start Date": "Mon, 28 Apr 2003 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "17.971",
        "First Name": "null",
        "Gender": "null",
        "Last Login Time": "9:59 AM",
        "Salary": 83895,
        "Senior Management": "null",
        "Start Date": "Fri, 25 Sep 1981 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "1.702",
        "First Name": "null",
        "Gender": "null",
        "Last Login Time": "12:49 PM",
        "Salary": 147309,
        "Senior Management": "null",
        "Start Date": "Fri, 02 Sep 1988 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "13.592",
        "First Name": "null",
        "Gender": "null",
        "Last Login Time": "3:39 AM",
        "Salary": 132505,
        "Senior Management": "null",
        "Start Date": "Mon, 15 Apr 1991 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "5.665",
        "First Name": "null",
        "Gender": "null",
        "Last Login Time": "1:35 AM",
        "Salary": 87103,
        "Senior Management": "null",
        "Start Date": "Mon, 01 Aug 1988 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "18.115",
        "First Name": "Amy",
        "Gender": "null",
        "Last Login Time": "10:52 AM",
        "Salary": 63888,
        "Senior Management": "true",
        "Start Date": "Tue, 25 Dec 1984 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "10.385",
        "First Name": "Amy",
        "Gender": "null",
        "Last Login Time": "11:47 AM",
        "Salary": 102839,
        "Senior Management": "true",
        "Start Date": "Sat, 19 May 1984 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "17.578",
        "First Name": "Alan",
        "Gender": "null",
        "Last Login Time": "1:28 PM",
        "Salary": 40341,
        "Senior Management": "true",
        "Start Date": "Mon, 03 Mar 2014 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "10.162",
        "First Name": "Anna",
        "Gender": "null",
        "Last Login Time": "9:19 AM",
        "Salary": 45418,
        "Senior Management": "false",
        "Start Date": "Wed, 13 Mar 1985 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "9.564",
        "First Name": "Anne",
        "Gender": "null",
        "Last Login Time": "11:57 PM",
        "Salary": 122762,
        "Senior Management": "false",
        "Start Date": "Thu, 18 Apr 1996 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "12.345",
        "First Name": "Carl",
        "Gender": "null",
        "Last Login Time": "3:57 AM",
        "Salary": 125104,
        "Senior Management": "false",
        "Start Date": "Fri, 07 Feb 2014 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "12.49",
        "First Name": "Carl",
        "Gender": "null",
        "Last Login Time": "8:11 AM",
        "Salary": 100888,
        "Senior Management": "true",
        "Start Date": "Sat, 26 Oct 1991 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "7.617",
        "First Name": "Carl",
        "Gender": "null",
        "Last Login Time": "8:01 AM",
        "Salary": 98295,
        "Senior Management": "true",
        "Start Date": "Sat, 18 Aug 2007 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "2.071",
        "First Name": "Carl",
        "Gender": "null",
        "Last Login Time": "7:54 AM",
        "Salary": 49325,
        "Senior Management": "true",
        "Start Date": "Thu, 11 Feb 1982 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "12.045",
        "First Name": "Fred",
        "Gender": "null",
        "Last Login Time": "2:03 PM",
        "Salary": 59937,
        "Senior Management": "true",
        "Start Date": "Sun, 02 Dec 1984 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "3.657",
        "First Name": "Joan",
        "Gender": "null",
        "Last Login Time": "12:22 PM",
        "Salary": 38712,
        "Senior Management": "false",
        "Start Date": "Fri, 25 Jul 1980 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "5.19",
        "First Name": "Judy",
        "Gender": "null",
        "Last Login Time": "3:38 PM",
        "Salary": 46829,
        "Senior Management": "true",
        "Start Date": "Fri, 15 Jul 2011 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "4.934",
        "First Name": "Lois",
        "Gender": "null",
        "Last Login Time": "7:18 PM",
        "Salary": 64714,
        "Senior Management": "true",
        "Start Date": "Sat, 22 Apr 1995 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "2.657",
        "First Name": "Mark",
        "Gender": "null",
        "Last Login Time": "12:27 PM",
        "Salary": 44836,
        "Senior Management": "false",
        "Start Date": "Sat, 09 Sep 2006 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "6.662",
        "First Name": "Mary",
        "Gender": "null",
        "Last Login Time": "7:02 PM",
        "Salary": 100341,
        "Senior Management": "false",
        "Start Date": "Wed, 24 Dec 1986 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "18.704",
        "First Name": "Paul",
        "Gender": "null",
        "Last Login Time": "12:23 PM",
        "Salary": 91462,
        "Senior Management": "false",
        "Start Date": "Fri, 18 Feb 2011 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "2.518",
        "First Name": "Ruth",
        "Gender": "null",
        "Last Login Time": "5:56 AM",
        "Salary": 98233,
        "Senior Management": "true",
        "Start Date": "Tue, 18 May 1999 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "18.863",
        "First Name": "Sara",
        "Gender": "null",
        "Last Login Time": "1:35 PM",
        "Salary": 87713,
        "Senior Management": "true",
        "Start Date": "Fri, 07 Oct 1983 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "14.344",
        "First Name": "Sara",
        "Gender": "null",
        "Last Login Time": "2:47 PM",
        "Salary": 135990,
        "Senior Management": "true",
        "Start Date": "Tue, 18 Nov 2014 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "6.617",
        "First Name": "Todd",
        "Gender": "null",
        "Last Login Time": "2:26 PM",
        "Salary": 84692,
        "Senior Management": "false",
        "Start Date": "Tue, 10 Jun 2003 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "18.424",
        "First Name": "Aaron",
        "Gender": "null",
        "Last Login Time": "7:39 PM",
        "Salary": 63126,
        "Senior Management": "false",
        "Start Date": "Wed, 22 Jan 1986 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "11.479",
        "First Name": "Alice",
        "Gender": "null",
        "Last Login Time": "6:35 AM",
        "Salary": 148339,
        "Senior Management": "true",
        "Start Date": "Sun, 23 Apr 1995 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "17.29",
        "First Name": "Annie",
        "Gender": "null",
        "Last Login Time": "12:11 AM",
        "Salary": 103495,
        "Senior Management": "true",
        "Start Date": "Sat, 29 Sep 2007 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "18.241",
        "First Name": "Billy",
        "Gender": "null",
        "Last Login Time": "8:21 AM",
        "Salary": 62913,
        "Senior Management": "true",
        "Start Date": "Tue, 16 Mar 2004 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "15.858",
        "First Name": "Bobby",
        "Gender": "null",
        "Last Login Time": "2:09 PM",
        "Salary": 108127,
        "Senior Management": "false",
        "Start Date": "Fri, 01 Sep 1995 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "15.704",
        "First Name": "Bobby",
        "Gender": "null",
        "Last Login Time": "3:50 PM",
        "Salary": 84232,
        "Senior Management": "true",
        "Start Date": "Mon, 21 Jul 2003 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "3.055",
        "First Name": "Chris",
        "Gender": "null",
        "Last Login Time": "12:13 PM",
        "Salary": 113590,
        "Senior Management": "false",
        "Start Date": "Thu, 24 Jan 1980 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "12.062",
        "First Name": "Frank",
        "Gender": "null",
        "Last Login Time": "10:18 AM",
        "Salary": 58563,
        "Senior Management": "true",
        "Start Date": "Tue, 20 Nov 2001 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "6.976",
        "First Name": "Harry",
        "Gender": "null",
        "Last Login Time": "5:45 AM",
        "Salary": 46240,
        "Senior Management": "true",
        "Start Date": "Thu, 05 Dec 1996 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "1.022",
        "First Name": "Helen",
        "Gender": "null",
        "Last Login Time": "1:42 PM",
        "Salary": 45724,
        "Senior Management": "false",
        "Start Date": "Thu, 02 Dec 1993 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "16.655",
        "First Name": "Henry",
        "Gender": "null",
        "Last Login Time": "6:09 AM",
        "Salary": 132483,
        "Senior Management": "false",
        "Start Date": "Sun, 23 Nov 2014 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "4.382",
        "First Name": "Irene",
        "Gender": "null",
        "Last Login Time": "4:31 PM",
        "Salary": 100863,
        "Senior Management": "true",
        "Start Date": "Tue, 14 Jul 2015 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "4.38",
        "First Name": "Irene",
        "Gender": "null",
        "Last Login Time": "10:23 PM",
        "Salary": 135369,
        "Senior Management": "false",
        "Start Date": "Thu, 28 Feb 1991 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "8.309",
        "First Name": "James",
        "Gender": "null",
        "Last Login Time": "11:00 PM",
        "Salary": 128771,
        "Senior Management": "false",
        "Start Date": "Wed, 26 Jan 2005 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "14.316",
        "First Name": "James",
        "Gender": "null",
        "Last Login Time": "10:52 PM",
        "Salary": 68501,
        "Senior Management": "false",
        "Start Date": "Tue, 22 Nov 1983 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "9.712",
        "First Name": "Janet",
        "Gender": "null",
        "Last Login Time": "5:48 AM",
        "Salary": 85789,
        "Senior Management": "false",
        "Start Date": "Sat, 25 Jan 1986 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "1.869",
        "First Name": "Jason",
        "Gender": "null",
        "Last Login Time": "1:20 AM",
        "Salary": 82873,
        "Senior Management": "false",
        "Start Date": "Thu, 06 Mar 2008 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "11.518",
        "First Name": "Jason",
        "Gender": "null",
        "Last Login Time": "8:16 PM",
        "Salary": 97480,
        "Senior Management": "false",
        "Start Date": "Fri, 15 Apr 1988 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "7.487",
        "First Name": "Jesse",
        "Gender": "null",
        "Last Login Time": "2:24 AM",
        "Salary": 98811,
        "Senior Management": "false",
        "Start Date": "Wed, 16 Jul 2014 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "7.175",
        "First Name": "Jimmy",
        "Gender": "null",
        "Last Login Time": "2:48 AM",
        "Salary": 86676,
        "Senior Management": "true",
        "Start Date": "Fri, 26 Aug 1983 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "12.752",
        "First Name": "Joyce",
        "Gender": "null",
        "Last Login Time": "2:40 PM",
        "Salary": 88657,
        "Senior Management": "false",
        "Start Date": "Sun, 20 Feb 2005 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "9.048",
        "First Name": "Julie",
        "Gender": "null",
        "Last Login Time": "5:35 PM",
        "Salary": 93302,
        "Senior Management": "true",
        "Start Date": "Thu, 04 Feb 1999 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "7.099",
        "First Name": "Julie",
        "Gender": "null",
        "Last Login Time": "1:15 AM",
        "Salary": 60361,
        "Senior Management": "true",
        "Start Date": "Sat, 21 Oct 2000 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "17.263",
        "First Name": "Julie",
        "Gender": "null",
        "Last Login Time": "6:31 AM",
        "Salary": 50529,
        "Senior Management": "false",
        "Start Date": "Thu, 08 May 1980 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "10.62",
        "First Name": "Laura",
        "Gender": "null",
        "Last Login Time": "9:23 PM",
        "Salary": 140371,
        "Senior Management": "true",
        "Start Date": "Sat, 19 Jul 2014 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "16.379",
        "First Name": "Louis",
        "Gender": "null",
        "Last Login Time": "6:39 PM",
        "Salary": 145274,
        "Senior Management": "false",
        "Start Date": "Sat, 05 Feb 1983 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "4",
        "First Name": "Maria",
        "Gender": "null",
        "Last Login Time": "8:36 PM",
        "Salary": 106562,
        "Senior Management": "false",
        "Start Date": "Sat, 18 Jan 1986 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "8.738",
        "First Name": "Maria",
        "Gender": "null",
        "Last Login Time": "1:48 AM",
        "Salary": 148857,
        "Senior Management": "false",
        "Start Date": "Wed, 19 Jun 1985 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "4.271",
        "First Name": "Paula",
        "Gender": "null",
        "Last Login Time": "2:01 PM",
        "Salary": 48866,
        "Senior Management": "false",
        "Start Date": "Wed, 23 Nov 2005 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "7.017",
        "First Name": "Peter",
        "Gender": "null",
        "Last Login Time": "5:59 PM",
        "Salary": 38989,
        "Senior Management": "true",
        "Start Date": "Thu, 03 Sep 1987 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "14.509",
        "First Name": "Peter",
        "Gender": "null",
        "Last Login Time": "9:33 PM",
        "Salary": 118840,
        "Senior Management": "true",
        "Start Date": "Mon, 13 Oct 2014 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "2.147",
        "First Name": "Ralph",
        "Gender": "null",
        "Last Login Time": "6:53 PM",
        "Salary": 70635,
        "Senior Management": "false",
        "Start Date": "Fri, 28 Jul 1995 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "8.94",
        "First Name": "Randy",
        "Gender": "null",
        "Last Login Time": "3:04 PM",
        "Salary": 133943,
        "Senior Management": "true",
        "Start Date": "Thu, 06 Feb 1986 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "6.611",
        "First Name": "Robin",
        "Gender": "null",
        "Last Login Time": "2:42 PM",
        "Salary": 41230,
        "Senior Management": "true",
        "Start Date": "Tue, 20 Dec 2005 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "11.712",
        "First Name": "Robin",
        "Gender": "null",
        "Last Login Time": "1:26 AM",
        "Salary": 93201,
        "Senior Management": "true",
        "Start Date": "Fri, 16 Sep 2005 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "14.603",
        "First Name": "Sarah",
        "Gender": "null",
        "Last Login Time": "1:08 PM",
        "Salary": 58295,
        "Senior Management": "true",
        "Start Date": "Thu, 21 Nov 1985 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "8.86",
        "First Name": "Sarah",
        "Gender": "null",
        "Last Login Time": "10:49 PM",
        "Salary": 109980,
        "Senior Management": "false",
        "Start Date": "Fri, 20 Jul 1990 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "9.047",
        "First Name": "Sarah",
        "Gender": "null",
        "Last Login Time": "2:51 PM",
        "Salary": 37748,
        "Senior Management": "false",
        "Start Date": "Mon, 31 Aug 1981 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "5.218",
        "First Name": "Scott",
        "Gender": "null",
        "Last Login Time": "6:58 PM",
        "Salary": 122367,
        "Senior Management": "false",
        "Start Date": "Thu, 11 Jul 1991 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "9.55",
        "First Name": "Steve",
        "Gender": "null",
        "Last Login Time": "3:55 AM",
        "Salary": 83159,
        "Senior Management": "true",
        "Start Date": "Sat, 23 Feb 2002 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "4.785",
        "First Name": "Steve",
        "Gender": "null",
        "Last Login Time": "3:41 PM",
        "Salary": 53692,
        "Senior Management": "true",
        "Start Date": "Thu, 27 Aug 2009 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "19.49",
        "First Name": "Terry",
        "Gender": "null",
        "Last Login Time": "12:29 AM",
        "Salary": 140002,
        "Senior Management": "true",
        "Start Date": "Fri, 15 Jul 2016 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "8.219",
        "First Name": "Terry",
        "Gender": "null",
        "Last Login Time": "4:41 PM",
        "Salary": 41238,
        "Senior Management": "false",
        "Start Date": "Fri, 11 Sep 1992 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "19.391",
        "First Name": "Amanda",
        "Gender": "null",
        "Last Login Time": "2:15 PM",
        "Salary": 46665,
        "Senior Management": "true",
        "Start Date": "Sun, 11 Aug 1991 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "15.108",
        "First Name": "Amanda",
        "Gender": "null",
        "Last Login Time": "9:17 AM",
        "Salary": 135118,
        "Senior Management": "false",
        "Start Date": "Tue, 16 Mar 2010 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "12.211",
        "First Name": "Bonnie",
        "Gender": "null",
        "Last Login Time": "6:52 PM",
        "Salary": 108946,
        "Senior Management": "false",
        "Start Date": "Wed, 18 Jan 2006 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "3.742",
        "First Name": "Brenda",
        "Gender": "null",
        "Last Login Time": "11:07 PM",
        "Salary": 106115,
        "Senior Management": "true",
        "Start Date": "Tue, 27 Jul 2010 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "19.062",
        "First Name": "Brenda",
        "Gender": "null",
        "Last Login Time": "6:32 AM",
        "Salary": 82439,
        "Senior Management": "false",
        "Start Date": "Wed, 29 May 1991 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "13.448",
        "First Name": "Ernest",
        "Gender": "null",
        "Last Login Time": "1:51 AM",
        "Salary": 72145,
        "Senior Management": "true",
        "Start Date": "Fri, 18 Jan 2002 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "8.999",
        "First Name": "George",
        "Gender": "null",
        "Last Login Time": "11:29 AM",
        "Salary": 38375,
        "Senior Management": "false",
        "Start Date": "Wed, 24 Feb 1988 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "15.602",
        "First Name": "Gerald",
        "Gender": "null",
        "Last Login Time": "12:50 AM",
        "Salary": 137126,
        "Senior Management": "true",
        "Start Date": "Fri, 17 Mar 1995 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "12.292",
        "First Name": "Gerald",
        "Gender": "null",
        "Last Login Time": "3:50 PM",
        "Salary": 133366,
        "Senior Management": "false",
        "Start Date": "Wed, 08 Jan 1992 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "17.426",
        "First Name": "Gerald",
        "Gender": "null",
        "Last Login Time": "12:44 PM",
        "Salary": 93712,
        "Senior Management": "true",
        "Start Date": "Sat, 15 Apr 1989 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "1.113",
        "First Name": "Gloria",
        "Gender": "null",
        "Last Login Time": "1:57 AM",
        "Salary": 140885,
        "Senior Management": "false",
        "Start Date": "Tue, 19 Jul 1983 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "7.776",
        "First Name": "Harold",
        "Gender": "null",
        "Last Login Time": "11:02 AM",
        "Salary": 79459,
        "Senior Management": "true",
        "Start Date": "Wed, 04 Feb 2004 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "11.583",
        "First Name": "Janice",
        "Gender": "null",
        "Last Login Time": "5:12 AM",
        "Salary": 91719,
        "Senior Management": "true",
        "Start Date": "Thu, 21 Aug 1997 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "16.968",
        "First Name": "Janice",
        "Gender": "null",
        "Last Login Time": "6:02 PM",
        "Salary": 139791,
        "Senior Management": "false",
        "Start Date": "Tue, 19 Nov 1991 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "3.18",
        "First Name": "Jeremy",
        "Gender": "null",
        "Last Login Time": "1:49 PM",
        "Salary": 55394,
        "Senior Management": "true",
        "Start Date": "Sun, 10 Nov 1996 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "11.879",
        "First Name": "Joseph",
        "Gender": "null",
        "Last Login Time": "1:05 PM",
        "Salary": 86564,
        "Senior Management": "true",
        "Start Date": "Sun, 28 Mar 1982 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "18.816",
        "First Name": "Joshua",
        "Gender": "null",
        "Last Login Time": "1:58 AM",
        "Salary": 90816,
        "Senior Management": "true",
        "Start Date": "Thu, 08 Mar 2012 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "13.865",
        "First Name": "Justin",
        "Gender": "null",
        "Last Login Time": "8:43 PM",
        "Salary": 96978,
        "Senior Management": "false",
        "Start Date": "Fri, 15 Apr 2005 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "3.794",
        "First Name": "Justin",
        "Gender": "null",
        "Last Login Time": "4:58 PM",
        "Salary": 38344,
        "Senior Management": "false",
        "Start Date": "Sun, 10 Feb 1991 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "15.745",
        "First Name": "Martin",
        "Gender": "null",
        "Last Login Time": "4:17 AM",
        "Salary": 123963,
        "Senior Management": "true",
        "Start Date": "Tue, 06 Feb 2001 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "12.452",
        "First Name": "Nicole",
        "Gender": "null",
        "Last Login Time": "2:28 PM",
        "Salary": 122717,
        "Senior Management": "false",
        "Start Date": "Fri, 05 Mar 1982 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "4.707",
        "First Name": "Nicole",
        "Gender": "null",
        "Last Login Time": "12:03 PM",
        "Salary": 41449,
        "Senior Management": "false",
        "Start Date": "Sat, 02 May 1981 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "5.66",
        "First Name": "Pamela",
        "Gender": "null",
        "Last Login Time": "1:33 PM",
        "Salary": 72979,
        "Senior Management": "false",
        "Start Date": "Sun, 15 Jul 2001 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "5.89",
        "First Name": "Robert",
        "Gender": "null",
        "Last Login Time": "1:20 AM",
        "Salary": 69267,
        "Senior Management": "true",
        "Start Date": "Mon, 04 Dec 2000 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "8.382",
        "First Name": "Robert",
        "Gender": "null",
        "Last Login Time": "3:17 AM",
        "Salary": 90998,
        "Senior Management": "false",
        "Start Date": "Fri, 25 May 2007 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "9.849",
        "First Name": "Samuel",
        "Gender": "null",
        "Last Login Time": "3:08 AM",
        "Salary": 141305,
        "Senior Management": "true",
        "Start Date": "Mon, 07 Oct 2002 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "6.513",
        "First Name": "Sharon",
        "Gender": "null",
        "Last Login Time": "3:46 AM",
        "Salary": 83658,
        "Senior Management": "false",
        "Start Date": "Thu, 01 Mar 1990 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "10.413",
        "First Name": "Sharon",
        "Gender": "null",
        "Last Login Time": "5:59 PM",
        "Salary": 97635,
        "Senior Management": "true",
        "Start Date": "Sun, 28 Oct 1984 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "8.689",
        "First Name": "Teresa",
        "Gender": "null",
        "Last Login Time": "10:55 AM",
        "Salary": 140013,
        "Senior Management": "true",
        "Start Date": "Thu, 28 Jan 2016 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "11.378",
        "First Name": "Teresa",
        "Gender": "null",
        "Last Login Time": "3:47 PM",
        "Salary": 63103,
        "Senior Management": "false",
        "Start Date": "Fri, 03 Jan 1992 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "3.95",
        "First Name": "Thomas",
        "Gender": "null",
        "Last Login Time": "8:31 PM",
        "Salary": 41549,
        "Senior Management": "false",
        "Start Date": "Thu, 31 Aug 1995 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "10.489",
        "First Name": "Victor",
        "Gender": "null",
        "Last Login Time": "8:40 PM",
        "Salary": 84546,
        "Senior Management": "true",
        "Start Date": "Thu, 10 Mar 2011 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "11.159",
        "First Name": "Victor",
        "Gender": "null",
        "Last Login Time": "2:49 PM",
        "Salary": 76381,
        "Senior Management": "true",
        "Start Date": "Fri, 28 Jul 2006 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "18.099",
        "First Name": "Walter",
        "Gender": "null",
        "Last Login Time": "10:33 PM",
        "Salary": 66757,
        "Senior Management": "false",
        "Start Date": "Tue, 21 Dec 1999 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "3.05",
        "First Name": "Antonio",
        "Gender": "null",
        "Last Login Time": "9:37 PM",
        "Salary": 103050,
        "Senior Management": "false",
        "Start Date": "Sun, 18 Jun 1989 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "16.475",
        "First Name": "Barbara",
        "Gender": "null",
        "Last Login Time": "7:32 PM",
        "Salary": 99326,
        "Senior Management": "true",
        "Start Date": "Sat, 03 May 2003 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "13.443",
        "First Name": "Barbara",
        "Gender": "null",
        "Last Login Time": "12:22 AM",
        "Salary": 94493,
        "Senior Management": "true",
        "Start Date": "Thu, 26 Apr 2001 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "14.764",
        "First Name": "Barbara",
        "Gender": "null",
        "Last Login Time": "11:04 PM",
        "Salary": 90187,
        "Senior Management": "true",
        "Start Date": "Wed, 10 Dec 1980 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "15.749",
        "First Name": "Barbara",
        "Gender": "null",
        "Last Login Time": "10:09 AM",
        "Salary": 90556,
        "Senior Management": "true",
        "Start Date": "Tue, 20 Dec 1994 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "8.218",
        "First Name": "Barbara",
        "Gender": "null",
        "Last Login Time": "5:13 AM",
        "Salary": 43312,
        "Senior Management": "true",
        "Start Date": "Fri, 02 Aug 2002 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "3.38",
        "First Name": "Beverly",
        "Gender": "null",
        "Last Login Time": "5:49 AM",
        "Salary": 104815,
        "Senior Management": "false",
        "Start Date": "Wed, 03 May 1995 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "15.295",
        "First Name": "Brandon",
        "Gender": "null",
        "Last Login Time": "8:17 PM",
        "Salary": 121333,
        "Senior Management": "false",
        "Start Date": "Mon, 03 Nov 1997 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "9.769",
        "First Name": "Brandon",
        "Gender": "null",
        "Last Login Time": "3:36 PM",
        "Salary": 73587,
        "Senior Management": "true",
        "Start Date": "Mon, 31 May 2004 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "11.416",
        "First Name": "Brandon",
        "Gender": "null",
        "Last Login Time": "2:32 AM",
        "Salary": 144187,
        "Senior Management": "true",
        "Start Date": "Sat, 05 Sep 1992 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "5.574",
        "First Name": "Charles",
        "Gender": "null",
        "Last Login Time": "1:00 PM",
        "Salary": 137171,
        "Senior Management": "true",
        "Start Date": "Sun, 01 Mar 1987 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "18.751",
        "First Name": "Cynthia",
        "Gender": "null",
        "Last Login Time": "10:40 PM",
        "Salary": 107816,
        "Senior Management": "false",
        "Start Date": "Tue, 19 Nov 1996 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "6.662",
        "First Name": "Deborah",
        "Gender": "null",
        "Last Login Time": "11:38 PM",
        "Salary": 101457,
        "Senior Management": "false",
        "Start Date": "Thu, 03 Feb 1983 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "14.771",
        "First Name": "Douglas",
        "Gender": "null",
        "Last Login Time": "2:03 AM",
        "Salary": 104496,
        "Senior Management": "true",
        "Start Date": "Wed, 04 Feb 2009 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "10.628",
        "First Name": "Gregory",
        "Gender": "null",
        "Last Login Time": "5:08 AM",
        "Salary": 98865,
        "Senior Management": "true",
        "Start Date": "Mon, 15 Jun 1992 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "4.805",
        "First Name": "Gregory",
        "Gender": "null",
        "Last Login Time": "11:31 PM",
        "Salary": 137661,
        "Senior Management": "true",
        "Start Date": "Sat, 09 Jul 2011 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "12.993",
        "First Name": "Jessica",
        "Gender": "null",
        "Last Login Time": "8:45 PM",
        "Salary": 121160,
        "Senior Management": "false",
        "Start Date": "Sat, 07 Mar 2015 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "10.146",
        "First Name": "Kenneth",
        "Gender": "null",
        "Last Login Time": "10:10 AM",
        "Salary": 95296,
        "Senior Management": "false",
        "Start Date": "Mon, 28 Feb 1994 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "17.612",
        "First Name": "Lillian",
        "Gender": "null",
        "Last Login Time": "3:43 PM",
        "Salary": 64164,
        "Senior Management": "false",
        "Start Date": "Thu, 12 May 2016 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "11.451",
        "First Name": "Marilyn",
        "Gender": "null",
        "Last Login Time": "9:09 AM",
        "Salary": 103386,
        "Senior Management": "false",
        "Start Date": "Sun, 22 Aug 1999 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "14.637",
        "First Name": "Matthew",
        "Gender": "null",
        "Last Login Time": "7:35 AM",
        "Salary": 79443,
        "Senior Management": "false",
        "Start Date": "Mon, 09 Jun 2003 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "14.837",
        "First Name": "Patrick",
        "Gender": "null",
        "Last Login Time": "2:24 AM",
        "Salary": 124488,
        "Senior Management": "true",
        "Start Date": "Sun, 14 Jul 1991 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "4.542",
        "First Name": "Patrick",
        "Gender": "null",
        "Last Login Time": "11:43 AM",
        "Salary": 137314,
        "Senior Management": "true",
        "Start Date": "Mon, 30 Aug 2004 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "2.277",
        "First Name": "Phillip",
        "Gender": "null",
        "Last Login Time": "11:09 AM",
        "Salary": 89700,
        "Senior Management": "true",
        "Start Date": "Mon, 20 Oct 2003 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "19.107",
        "First Name": "Phyllis",
        "Gender": "null",
        "Last Login Time": "7:05 PM",
        "Salary": 94088,
        "Senior Management": "false",
        "Start Date": "Sat, 21 Apr 1984 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "6.007",
        "First Name": "Phyllis",
        "Gender": "null",
        "Last Login Time": "7:11 AM",
        "Salary": 99150,
        "Senior Management": "false",
        "Start Date": "Fri, 25 Oct 1985 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "14.272",
        "First Name": "Richard",
        "Gender": "null",
        "Last Login Time": "5:05 PM",
        "Salary": 124655,
        "Senior Management": "true",
        "Start Date": "Sat, 28 Nov 1992 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "12.396",
        "First Name": "Russell",
        "Gender": "null",
        "Last Login Time": "7:57 AM",
        "Salary": 133980,
        "Senior Management": "true",
        "Start Date": "Thu, 05 May 1988 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "3.533",
        "First Name": "Russell",
        "Gender": "null",
        "Last Login Time": "11:59 AM",
        "Salary": 149456,
        "Senior Management": "false",
        "Start Date": "Sat, 09 May 2009 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "12.699",
        "First Name": "Shirley",
        "Gender": "null",
        "Last Login Time": "6:01 PM",
        "Salary": 67811,
        "Senior Management": "false",
        "Start Date": "Fri, 16 Nov 1990 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "1.909",
        "First Name": "Stephen",
        "Gender": "null",
        "Last Login Time": "8:10 PM",
        "Salary": 85668,
        "Senior Management": "false",
        "Start Date": "Sun, 10 Jul 1983 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "3.319",
        "First Name": "Theresa",
        "Gender": "null",
        "Last Login Time": "10:16 AM",
        "Salary": 42025,
        "Senior Management": "true",
        "Start Date": "Sat, 07 Oct 1995 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "16.231",
        "First Name": "Jennifer",
        "Gender": "null",
        "Last Login Time": "8:38 PM",
        "Salary": 58520,
        "Senior Management": "true",
        "Start Date": "Tue, 24 Jan 1989 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "18.771",
        "First Name": "Kathleen",
        "Gender": "null",
        "Last Login Time": "6:46 PM",
        "Salary": 77834,
        "Senior Management": "false",
        "Start Date": "Wed, 11 Apr 1990 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "18.74",
        "First Name": "Kathleen",
        "Gender": "null",
        "Last Login Time": "8:55 AM",
        "Salary": 119735,
        "Senior Management": "false",
        "Start Date": "Mon, 09 May 2016 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "16.353",
        "First Name": "Michelle",
        "Gender": "null",
        "Last Login Time": "6:28 AM",
        "Salary": 124441,
        "Senior Management": "false",
        "Start Date": "Sat, 31 Mar 2012 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "6.525",
        "First Name": "Nicholas",
        "Gender": "null",
        "Last Login Time": "7:12 PM",
        "Salary": 58478,
        "Senior Management": "true",
        "Start Date": "Sat, 09 Sep 1989 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "1.601",
        "First Name": "Virginia",
        "Gender": "null",
        "Last Login Time": "5:58 PM",
        "Salary": 111858,
        "Senior Management": "true",
        "Start Date": "Sat, 07 May 1994 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "11.308",
        "First Name": "Christine",
        "Gender": "null",
        "Last Login Time": "1:08 AM",
        "Salary": 66582,
        "Senior Management": "true",
        "Start Date": "Sun, 28 Jun 2015 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "9.862",
        "First Name": "Christine",
        "Gender": "null",
        "Last Login Time": "6:00 PM",
        "Salary": 50366,
        "Senior Management": "true",
        "Start Date": "Sun, 15 Jun 1980 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "12.525",
        "First Name": "Elizabeth",
        "Gender": "null",
        "Last Login Time": "3:58 AM",
        "Salary": 52730,
        "Senior Management": "false",
        "Start Date": "Mon, 16 Feb 1981 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "5.042",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "4:19 PM",
        "Salary": 125792,
        "Senior Management": "null",
        "Start Date": "Thu, 14 Jun 2012 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "18.576",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "1:12 AM",
        "Salary": 37076,
        "Senior Management": "null",
        "Start Date": "Mon, 08 Oct 2012 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "6.417",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "2:27 PM",
        "Salary": 122340,
        "Senior Management": "null",
        "Start Date": "Fri, 21 Aug 1998 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "7.797",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "2:33 AM",
        "Salary": 122173,
        "Senior Management": "null",
        "Start Date": "Fri, 29 Jan 2016 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "18.988",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "8:58 PM",
        "Salary": 76189,
        "Senior Management": "null",
        "Start Date": "Sat, 22 Jun 1991 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "15.517",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "6:16 AM",
        "Salary": 42676,
        "Senior Management": "null",
        "Start Date": "Thu, 25 Nov 1999 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "16.044",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "1:01 PM",
        "Salary": 40451,
        "Senior Management": "null",
        "Start Date": "Fri, 04 Feb 2005 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "14.987",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "2:57 AM",
        "Salary": 87760,
        "Senior Management": "null",
        "Start Date": "Wed, 27 Jan 2010 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "4.844",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "9:29 AM",
        "Salary": 69906,
        "Senior Management": "null",
        "Start Date": "Sun, 09 Oct 2011 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "3.095",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "9:36 PM",
        "Salary": 65078,
        "Senior Management": "null",
        "Start Date": "Tue, 22 Apr 1997 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "5.966",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "5:23 AM",
        "Salary": 111043,
        "Senior Management": "null",
        "Start Date": "Sun, 29 Jun 2008 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "7.008",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "9:17 PM",
        "Salary": 76409,
        "Senior Management": "null",
        "Start Date": "Tue, 24 May 2016 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "10.429",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "12:26 AM",
        "Salary": 136602,
        "Senior Management": "null",
        "Start Date": "Tue, 21 Feb 1995 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "13.248",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "1:17 PM",
        "Salary": 71520,
        "Senior Management": "null",
        "Start Date": "Sun, 20 Apr 1980 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "12.74",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "11:59 PM",
        "Salary": 139754,
        "Senior Management": "null",
        "Start Date": "Thu, 13 Oct 1983 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "1.932",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "7:56 PM",
        "Salary": 88733,
        "Senior Management": "null",
        "Start Date": "Tue, 28 Aug 2012 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "19.387",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "9:37 AM",
        "Salary": 88086,
        "Senior Management": "null",
        "Start Date": "Fri, 20 Oct 1989 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "8.992",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "7:07 AM",
        "Salary": 139959,
        "Senior Management": "null",
        "Start Date": "Fri, 27 Dec 1996 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "9.801",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "2:09 AM",
        "Salary": 136655,
        "Senior Management": "null",
        "Start Date": "Wed, 23 May 1990 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "12.048",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "4:32 AM",
        "Salary": 60411,
        "Senior Management": "null",
        "Start Date": "Fri, 07 Apr 1995 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "3.655",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "1:00 PM",
        "Salary": 136681,
        "Senior Management": "null",
        "Start Date": "Wed, 17 Jun 2009 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "10.736",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "9:23 AM",
        "Salary": 47176,
        "Senior Management": "null",
        "Start Date": "Fri, 24 Oct 1986 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "17.68",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "4:41 PM",
        "Salary": 74104,
        "Senior Management": "null",
        "Start Date": "Tue, 06 May 1986 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "5.478",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "10:34 AM",
        "Salary": 141311,
        "Senior Management": "null",
        "Start Date": "Tue, 13 Dec 1994 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "9.494",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "2:30 PM",
        "Salary": 109411,
        "Senior Management": "null",
        "Start Date": "Thu, 12 Nov 2009 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "13.823",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "7:36 AM",
        "Salary": 114896,
        "Senior Management": "null",
        "Start Date": "Fri, 05 Sep 1980 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "7.1",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "3:11 AM",
        "Salary": 145329,
        "Senior Management": "null",
        "Start Date": "Tue, 24 Nov 2015 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "6.322",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "7:52 PM",
        "Salary": 103877,
        "Senior Management": "null",
        "Start Date": "Wed, 23 May 2001 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "5.329",
        "First Name": "null",
        "Gender": "Male",
        "Last Login Time": "3:07 PM",
        "Salary": 107351,
        "Senior Management": "null",
        "Start Date": "Mon, 30 Jul 2012 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "1.62",
        "First Name": "Joe",
        "Gender": "Male",
        "Last Login Time": "4:20 PM",
        "Salary": 144082,
        "Senior Management": "true",
        "Start Date": "Sun, 05 Dec 2010 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "11.119",
        "First Name": "Joe",
        "Gender": "Male",
        "Last Login Time": "3:14 PM",
        "Salary": 50645,
        "Senior Management": "false",
        "Start Date": "Fri, 14 Apr 2000 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "8.13",
        "First Name": "Joe",
        "Gender": "Male",
        "Last Login Time": "7:32 AM",
        "Salary": 62161,
        "Senior Management": "true",
        "Start Date": "Mon, 04 Jul 1983 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "1.02",
        "First Name": "Joe",
        "Gender": "Male",
        "Last Login Time": "10:28 AM",
        "Salary": 126120,
        "Senior Management": "false",
        "Start Date": "Tue, 08 Dec 1998 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "1.148",
        "First Name": "Joe",
        "Gender": "Male",
        "Last Login Time": "4:06 PM",
        "Salary": 119667,
        "Senior Management": "true",
        "Start Date": "Sat, 19 Jan 1980 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "3.45",
        "First Name": "Roy",
        "Gender": "Male",
        "Last Login Time": "1:31 PM",
        "Salary": 101941,
        "Senior Management": "false",
        "Start Date": "Thu, 23 Sep 2004 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "1.841",
        "First Name": "Roy",
        "Gender": "Male",
        "Last Login Time": "7:52 AM",
        "Salary": 148225,
        "Senior Management": "false",
        "Start Date": "Sun, 06 Aug 2006 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "12.942",
        "First Name": "Roy",
        "Gender": "Male",
        "Last Login Time": "1:22 PM",
        "Salary": 46875,
        "Senior Management": "true",
        "Start Date": "Mon, 10 May 2004 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "15.12",
        "First Name": "Adam",
        "Gender": "Male",
        "Last Login Time": "1:45 AM",
        "Salary": 95327,
        "Senior Management": "false",
        "Start Date": "Sat, 21 May 2011 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "14.727",
        "First Name": "Adam",
        "Gender": "Male",
        "Last Login Time": "8:57 PM",
        "Salary": 110194,
        "Senior Management": "true",
        "Start Date": "Mon, 24 Dec 1990 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "5.027",
        "First Name": "Adam",
        "Gender": "Male",
        "Last Login Time": "11:59 AM",
        "Salary": 71276,
        "Senior Management": "true",
        "Start Date": "Thu, 05 Jul 2007 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "3.491",
        "First Name": "Adam",
        "Gender": "Male",
        "Last Login Time": "9:53 PM",
        "Salary": 45181,
        "Senior Management": "false",
        "Start Date": "Fri, 08 Oct 2010 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "3.592",
        "First Name": "Alan",
        "Gender": "Male",
        "Last Login Time": "3:54 AM",
        "Salary": 111786,
        "Senior Management": "true",
        "Start Date": "Sun, 26 Jun 1988 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "10.084",
        "First Name": "Alan",
        "Gender": "Male",
        "Last Login Time": "12:26 AM",
        "Salary": 41453,
        "Senior Management": "false",
        "Start Date": "Fri, 17 Feb 2012 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "16.084",
        "First Name": "Carl",
        "Gender": "Male",
        "Last Login Time": "5:55 PM",
        "Salary": 130276,
        "Senior Management": "true",
        "Start Date": "Wed, 03 May 2006 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "19.289",
        "First Name": "Carl",
        "Gender": "Male",
        "Last Login Time": "5:59 PM",
        "Salary": 75598,
        "Senior Management": "false",
        "Start Date": "Mon, 30 Mar 1987 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "11.411",
        "First Name": "Carl",
        "Gender": "Male",
        "Last Login Time": "8:49 PM",
        "Salary": 63395,
        "Senior Management": "false",
        "Start Date": "Fri, 14 Dec 1984 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "15.528",
        "First Name": "Carl",
        "Gender": "Male",
        "Last Login Time": "1:33 PM",
        "Salary": 54033,
        "Senior Management": "true",
        "Start Date": "Wed, 07 Jul 2010 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "4.035",
        "First Name": "Earl",
        "Gender": "Male",
        "Last Login Time": "5:46 PM",
        "Salary": 91344,
        "Senior Management": "true",
        "Start Date": "Wed, 05 Jan 2000 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "13.773",
        "First Name": "Earl",
        "Gender": "Male",
        "Last Login Time": "9:03 PM",
        "Salary": 52620,
        "Senior Management": "false",
        "Start Date": "Tue, 11 Feb 2014 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "7.737",
        "First Name": "Earl",
        "Gender": "Male",
        "Last Login Time": "3:00 AM",
        "Salary": 48046,
        "Senior Management": "false",
        "Start Date": "Sat, 15 Jun 2013 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "11.513",
        "First Name": "Eric",
        "Gender": "Male",
        "Last Login Time": "9:16 PM",
        "Salary": 65168,
        "Senior Management": "false",
        "Start Date": "Fri, 12 Nov 2004 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "13.806",
        "First Name": "Eric",
        "Gender": "Male",
        "Last Login Time": "3:56 AM",
        "Salary": 51070,
        "Senior Management": "true",
        "Start Date": "Tue, 15 Jun 1993 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "18.225",
        "First Name": "Fred",
        "Gender": "Male",
        "Last Login Time": "2:25 AM",
        "Salary": 74129,
        "Senior Management": "false",
        "Start Date": "Wed, 20 Feb 1980 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "18.645",
        "First Name": "Fred",
        "Gender": "Male",
        "Last Login Time": "2:15 PM",
        "Salary": 121723,
        "Senior Management": "true",
        "Start Date": "Fri, 13 Feb 1987 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "11.058",
        "First Name": "Fred",
        "Gender": "Male",
        "Last Login Time": "2:27 AM",
        "Salary": 129712,
        "Senior Management": "false",
        "Start Date": "Fri, 03 Mar 1989 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "5.831",
        "First Name": "Gary",
        "Gender": "Male",
        "Last Login Time": "11:40 PM",
        "Salary": 109831,
        "Senior Management": "false",
        "Start Date": "Sun, 27 Jan 2008 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "8.525",
        "First Name": "Gary",
        "Gender": "Male",
        "Last Login Time": "12:04 AM",
        "Salary": 89661,
        "Senior Management": "false",
        "Start Date": "Wed, 12 Aug 1987 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "11.9",
        "First Name": "Gary",
        "Gender": "Male",
        "Last Login Time": "8:12 AM",
        "Salary": 49101,
        "Senior Management": "true",
        "Start Date": "Thu, 18 Aug 2011 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "12.159",
        "First Name": "Jack",
        "Gender": "Male",
        "Last Login Time": "5:51 AM",
        "Salary": 103902,
        "Senior Management": "false",
        "Start Date": "Sun, 12 Jan 1997 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "15.723",
        "First Name": "Jack",
        "Gender": "Male",
        "Last Login Time": "10:58 PM",
        "Salary": 106995,
        "Senior Management": "false",
        "Start Date": "Wed, 24 Dec 1980 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "18.266",
        "First Name": "Jack",
        "Gender": "Male",
        "Last Login Time": "3:17 AM",
        "Salary": 70367,
        "Senior Management": "true",
        "Start Date": "Wed, 30 May 2012 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "13.873",
        "First Name": "John",
        "Gender": "Male",
        "Last Login Time": "10:08 PM",
        "Salary": 97950,
        "Senior Management": "false",
        "Start Date": "Wed, 01 Jul 1992 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "19.305",
        "First Name": "John",
        "Gender": "Male",
        "Last Login Time": "7:01 AM",
        "Salary": 80740,
        "Senior Management": "false",
        "Start Date": "Sat, 23 Dec 1989 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "5.809",
        "First Name": "John",
        "Gender": "Male",
        "Last Login Time": "12:17 AM",
        "Salary": 66077,
        "Senior Management": "true",
        "Start Date": "Sun, 22 Jan 1995 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "13.001",
        "First Name": "John",
        "Gender": "Male",
        "Last Login Time": "3:07 AM",
        "Salary": 67165,
        "Senior Management": "false",
        "Start Date": "Fri, 29 Jan 1999 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "11.738",
        "First Name": "John",
        "Gender": "Male",
        "Last Login Time": "10:35 PM",
        "Salary": 146907,
        "Senior Management": "false",
        "Start Date": "Thu, 23 Dec 1982 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "14.33",
        "First Name": "Jose",
        "Gender": "Male",
        "Last Login Time": "1:39 PM",
        "Salary": 84834,
        "Senior Management": "true",
        "Start Date": "Sat, 30 Oct 2004 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "3.269",
        "First Name": "Jose",
        "Gender": "Male",
        "Last Login Time": "9:15 AM",
        "Salary": 59862,
        "Senior Management": "false",
        "Start Date": "Thu, 11 Jul 2002 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "3.595",
        "First Name": "Juan",
        "Gender": "Male",
        "Last Login Time": "11:09 PM",
        "Salary": 97364,
        "Senior Management": "false",
        "Start Date": "Tue, 16 Apr 2002 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "9.16",
        "First Name": "Juan",
        "Gender": "Male",
        "Last Login Time": "8:52 AM",
        "Salary": 85871,
        "Senior Management": "false",
        "Start Date": "Wed, 06 Oct 1993 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "5.025",
        "First Name": "Mark",
        "Gender": "Male",
        "Last Login Time": "5:40 PM",
        "Salary": 57286,
        "Senior Management": "true",
        "Start Date": "Sat, 12 Apr 2008 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "17.44",
        "First Name": "Mark",
        "Gender": "Male",
        "Last Login Time": "1:21 PM",
        "Salary": 121477,
        "Senior Management": "true",
        "Start Date": "Sun, 01 Apr 1984 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "12.182",
        "First Name": "Mark",
        "Gender": "Male",
        "Last Login Time": "2:37 PM",
        "Salary": 75150,
        "Senior Management": "true",
        "Start Date": "Mon, 22 Jan 2007 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "6.752",
        "First Name": "Mark",
        "Gender": "Male",
        "Last Login Time": "5:31 AM",
        "Salary": 95728,
        "Senior Management": "true",
        "Start Date": "Wed, 03 Oct 1984 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "3.046",
        "First Name": "Paul",
        "Gender": "Male",
        "Last Login Time": "7:25 PM",
        "Salary": 42146,
        "Senior Management": "false",
        "Start Date": "Wed, 04 Aug 1993 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "12.299",
        "First Name": "Paul",
        "Gender": "Male",
        "Last Login Time": "3:05 PM",
        "Salary": 41054,
        "Senior Management": "false",
        "Start Date": "Tue, 03 Jun 2008 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "11.466",
        "First Name": "Ryan",
        "Gender": "Male",
        "Last Login Time": "10:18 PM",
        "Salary": 139917,
        "Senior Management": "false",
        "Start Date": "Tue, 20 Jul 1993 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "17.499",
        "First Name": "Ryan",
        "Gender": "Male",
        "Last Login Time": "5:18 AM",
        "Salary": 91109,
        "Senior Management": "true",
        "Start Date": "Fri, 15 Apr 1988 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "6.01",
        "First Name": "Ryan",
        "Gender": "Male",
        "Last Login Time": "1:47 PM",
        "Salary": 57292,
        "Senior Management": "false",
        "Start Date": "Fri, 16 Nov 2012 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "19.475",
        "First Name": "Ryan",
        "Gender": "Male",
        "Last Login Time": "3:41 AM",
        "Salary": 85858,
        "Senior Management": "false",
        "Start Date": "Tue, 27 Apr 1999 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "19.934",
        "First Name": "Sean",
        "Gender": "Male",
        "Last Login Time": "8:59 PM",
        "Salary": 135490,
        "Senior Management": "false",
        "Start Date": "Sat, 04 May 1996 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "9.765",
        "First Name": "Sean",
        "Gender": "Male",
        "Last Login Time": "7:07 PM",
        "Salary": 42748,
        "Senior Management": "false",
        "Start Date": "Mon, 11 Feb 2013 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "9.634",
        "First Name": "Sean",
        "Gender": "Male",
        "Last Login Time": "4:51 PM",
        "Salary": 108581,
        "Senior Management": "false",
        "Start Date": "Tue, 25 Apr 2006 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "8.957",
        "First Name": "Sean",
        "Gender": "Male",
        "Last Login Time": "11:38 AM",
        "Salary": 131423,
        "Senior Management": "false",
        "Start Date": "Sat, 21 Mar 2009 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "11.178",
        "First Name": "Sean",
        "Gender": "Male",
        "Last Login Time": "2:23 PM",
        "Salary": 66146,
        "Senior Management": "false",
        "Start Date": "Mon, 17 Jan 1983 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "1.695",
        "First Name": "Todd",
        "Gender": "Male",
        "Last Login Time": "2:41 AM",
        "Salary": 49339,
        "Senior Management": "true",
        "Start Date": "Sun, 18 Feb 1990 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "11.226",
        "First Name": "Todd",
        "Gender": "Male",
        "Last Login Time": "10:31 AM",
        "Salary": 59728,
        "Senior Management": "true",
        "Start Date": "Tue, 13 Apr 1999 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "1.612",
        "First Name": "Todd",
        "Gender": "Male",
        "Last Login Time": "3:43 AM",
        "Salary": 107281,
        "Senior Management": "true",
        "Start Date": "Wed, 11 Mar 2009 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "10.985",
        "First Name": "Todd",
        "Gender": "Male",
        "Last Login Time": "10:13 AM",
        "Salary": 69989,
        "Senior Management": "true",
        "Start Date": "Thu, 02 Feb 1984 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "1.844",
        "First Name": "Todd",
        "Gender": "Male",
        "Last Login Time": "4:14 PM",
        "Salary": 85074,
        "Senior Management": "false",
        "Start Date": "Mon, 23 May 2011 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "3.56",
        "First Name": "Todd",
        "Gender": "Male",
        "Last Login Time": "2:45 PM",
        "Salary": 134408,
        "Senior Management": "true",
        "Start Date": "Wed, 16 Mar 2016 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "15.91",
        "First Name": "Todd",
        "Gender": "Male",
        "Last Login Time": "11:29 AM",
        "Salary": 103405,
        "Senior Management": "false",
        "Start Date": "Tue, 16 Feb 2010 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "18.473",
        "First Name": "Todd",
        "Gender": "Male",
        "Last Login Time": "6:53 PM",
        "Salary": 128175,
        "Senior Management": "true",
        "Start Date": "Sun, 04 Jul 1993 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "6.716",
        "First Name": "Todd",
        "Gender": "Male",
        "Last Login Time": "12:34 PM",
        "Salary": 115566,
        "Senior Management": "true",
        "Start Date": "Tue, 04 Jan 1983 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "11.849",
        "First Name": "Aaron",
        "Gender": "Male",
        "Last Login Time": "10:20 AM",
        "Salary": 61602,
        "Senior Management": "true",
        "Start Date": "Fri, 17 Feb 2012 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "5.097",
        "First Name": "Aaron",
        "Gender": "Male",
        "Last Login Time": "6:48 PM",
        "Salary": 58755,
        "Senior Management": "true",
        "Start Date": "Sat, 29 Jan 1994 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "11.343",
        "First Name": "Aaron",
        "Gender": "Male",
        "Last Login Time": "2:53 PM",
        "Salary": 52119,
        "Senior Management": "true",
        "Start Date": "Sun, 22 Jul 1990 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "7.768",
        "First Name": "Billy",
        "Gender": "Male",
        "Last Login Time": "12:05 PM",
        "Salary": 120444,
        "Senior Management": "true",
        "Start Date": "Mon, 13 Mar 1995 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "10.069",
        "First Name": "Billy",
        "Gender": "Male",
        "Last Login Time": "3:32 PM",
        "Salary": 144709,
        "Senior Management": "true",
        "Start Date": "Fri, 01 Dec 2006 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "9.153",
        "First Name": "Billy",
        "Gender": "Male",
        "Last Login Time": "3:14 PM",
        "Salary": 115280,
        "Senior Management": "false",
        "Start Date": "Thu, 06 Apr 2000 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "3.833",
        "First Name": "Bobby",
        "Gender": "Male",
        "Last Login Time": "10:01 AM",
        "Salary": 54043,
        "Senior Management": "false",
        "Start Date": "Mon, 07 May 2007 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "17.445",
        "First Name": "Bobby",
        "Gender": "Male",
        "Last Login Time": "1:29 AM",
        "Salary": 51685,
        "Senior Management": "true",
        "Start Date": "Fri, 23 Sep 1994 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "6.338",
        "First Name": "Bobby",
        "Gender": "Male",
        "Last Login Time": "5:40 PM",
        "Salary": 112117,
        "Senior Management": "false",
        "Start Date": "Sun, 31 Mar 1996 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "18.784",
        "First Name": "Bobby",
        "Gender": "Male",
        "Last Login Time": "10:52 PM",
        "Salary": 79047,
        "Senior Management": "false",
        "Start Date": "Thu, 30 Sep 2004 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "2.88",
        "First Name": "Bobby",
        "Gender": "Male",
        "Last Login Time": "7:40 AM",
        "Salary": 93368,
        "Senior Management": "true",
        "Start Date": "Tue, 05 Jun 1984 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "16.158",
        "First Name": "Bobby",
        "Gender": "Male",
        "Last Login Time": "1:16 AM",
        "Salary": 147842,
        "Senior Management": "true",
        "Start Date": "Mon, 19 Aug 1996 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "17.821",
        "First Name": "Brian",
        "Gender": "Male",
        "Last Login Time": "10:47 PM",
        "Salary": 93901,
        "Senior Management": "true",
        "Start Date": "Sat, 07 Apr 2007 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "6.796",
        "First Name": "Bruce",
        "Gender": "Male",
        "Last Login Time": "10:47 PM",
        "Salary": 114796,
        "Senior Management": "false",
        "Start Date": "Sat, 28 Nov 2009 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "15.427",
        "First Name": "Bruce",
        "Gender": "Male",
        "Last Login Time": "11:13 PM",
        "Salary": 141335,
        "Senior Management": "true",
        "Start Date": "Fri, 15 Mar 2013 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "13.926",
        "First Name": "Bruce",
        "Gender": "Male",
        "Last Login Time": "11:10 PM",
        "Salary": 134988,
        "Senior Management": "true",
        "Start Date": "Sun, 28 Jan 2007 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "12.391",
        "First Name": "Bruce",
        "Gender": "Male",
        "Last Login Time": "8:00 PM",
        "Salary": 35802,
        "Senior Management": "true",
        "Start Date": "Wed, 07 May 1980 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "1.496",
        "First Name": "Chris",
        "Gender": "Male",
        "Last Login Time": "1:57 AM",
        "Salary": 71642,
        "Senior Management": "false",
        "Start Date": "Tue, 12 Dec 2006 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "7.757",
        "First Name": "Craig",
        "Gender": "Male",
        "Last Login Time": "7:45 AM",
        "Salary": 37598,
        "Senior Management": "true",
        "Start Date": "Sun, 27 Feb 2000 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "19.642",
        "First Name": "Craig",
        "Gender": "Male",
        "Last Login Time": "4:45 AM",
        "Salary": 113506,
        "Senior Management": "false",
        "Start Date": "Wed, 08 Feb 1984 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "7.996",
        "First Name": "Craig",
        "Gender": "Male",
        "Last Login Time": "9:17 AM",
        "Salary": 125556,
        "Senior Management": "false",
        "Start Date": "Sun, 14 Apr 1996 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "13.266",
        "First Name": "Craig",
        "Gender": "Male",
        "Last Login Time": "11:31 PM",
        "Salary": 44857,
        "Senior Management": "false",
        "Start Date": "Tue, 01 Nov 2005 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "4.225",
        "First Name": "Craig",
        "Gender": "Male",
        "Last Login Time": "2:38 AM",
        "Salary": 123876,
        "Senior Management": "false",
        "Start Date": "Mon, 21 Aug 1995 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "15.407",
        "First Name": "David",
        "Gender": "Male",
        "Last Login Time": "8:48 AM",
        "Salary": 92242,
        "Senior Management": "false",
        "Start Date": "Sat, 05 Dec 2009 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "8.037",
        "First Name": "Frank",
        "Gender": "Male",
        "Last Login Time": "1:30 PM",
        "Salary": 71853,
        "Senior Management": "true",
        "Start Date": "Sat, 10 Jan 1981 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "17.07",
        "First Name": "Frank",
        "Gender": "Male",
        "Last Login Time": "12:04 PM",
        "Salary": 140303,
        "Senior Management": "false",
        "Start Date": "Sun, 27 Apr 2003 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "17.398",
        "First Name": "Frank",
        "Gender": "Male",
        "Last Login Time": "6:10 PM",
        "Salary": 75147,
        "Senior Management": "false",
        "Start Date": "Sat, 23 Nov 2002 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "7.927",
        "First Name": "Frank",
        "Gender": "Male",
        "Last Login Time": "9:15 PM",
        "Salary": 78891,
        "Senior Management": "true",
        "Start Date": "Mon, 02 Mar 2009 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "5.681",
        "First Name": "Frank",
        "Gender": "Male",
        "Last Login Time": "4:32 PM",
        "Salary": 91406,
        "Senior Management": "true",
        "Start Date": "Sat, 27 Jul 2013 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "7.03",
        "First Name": "Harry",
        "Gender": "Male",
        "Last Login Time": "3:16 PM",
        "Salary": 130620,
        "Senior Management": "false",
        "Start Date": "Wed, 26 Aug 1981 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "15.266",
        "First Name": "Harry",
        "Gender": "Male",
        "Last Login Time": "7:47 PM",
        "Salary": 64579,
        "Senior Management": "true",
        "Start Date": "Thu, 01 Oct 2015 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "18.089",
        "First Name": "Harry",
        "Gender": "Male",
        "Last Login Time": "8:18 PM",
        "Salary": 65482,
        "Senior Management": "false",
        "Start Date": "Sun, 27 Jan 1985 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "10.2",
        "First Name": "Harry",
        "Gender": "Male",
        "Last Login Time": "11:25 AM",
        "Salary": 59277,
        "Senior Management": "false",
        "Start Date": "Fri, 19 Nov 1982 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "15.193",
        "First Name": "Harry",
        "Gender": "Male",
        "Last Login Time": "1:36 AM",
        "Salary": 129148,
        "Senior Management": "true",
        "Start Date": "Wed, 23 Sep 2015 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "10.411",
        "First Name": "Harry",
        "Gender": "Male",
        "Last Login Time": "7:46 PM",
        "Salary": 63046,
        "Senior Management": "false",
        "Start Date": "Sun, 10 Feb 1985 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "16.455",
        "First Name": "Harry",
        "Gender": "Male",
        "Last Login Time": "6:31 PM",
        "Salary": 67656,
        "Senior Management": "true",
        "Start Date": "Tue, 30 Aug 2011 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "15.107",
        "First Name": "Henry",
        "Gender": "Male",
        "Last Login Time": "1:44 AM",
        "Salary": 64715,
        "Senior Management": "true",
        "Start Date": "Wed, 26 Jun 1996 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "19.687",
        "First Name": "Henry",
        "Gender": "Male",
        "Last Login Time": "4:18 AM",
        "Salary": 43542,
        "Senior Management": "false",
        "Start Date": "Mon, 24 Apr 1995 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "15.585",
        "First Name": "Henry",
        "Gender": "Male",
        "Last Login Time": "8:34 AM",
        "Salary": 89258,
        "Senior Management": "true",
        "Start Date": "Mon, 06 Feb 1995 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "1.432",
        "First Name": "Henry",
        "Gender": "Male",
        "Last Login Time": "2:04 AM",
        "Salary": 59943,
        "Senior Management": "false",
        "Start Date": "Mon, 12 May 1986 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "18.338",
        "First Name": "Henry",
        "Gender": "Male",
        "Last Login Time": "3:24 AM",
        "Salary": 49665,
        "Senior Management": "false",
        "Start Date": "Fri, 23 Feb 2007 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "13.023",
        "First Name": "James",
        "Gender": "Male",
        "Last Login Time": "8:52 PM",
        "Salary": 72257,
        "Senior Management": "false",
        "Start Date": "Sat, 11 Jul 2015 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "5.778",
        "First Name": "James",
        "Gender": "Male",
        "Last Login Time": "3:48 AM",
        "Salary": 74086,
        "Senior Management": "true",
        "Start Date": "Sun, 22 Nov 1998 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "17.105",
        "First Name": "James",
        "Gender": "Male",
        "Last Login Time": "7:06 AM",
        "Salary": 67789,
        "Senior Management": "true",
        "Start Date": "Wed, 05 Dec 2001 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "14.625",
        "First Name": "James",
        "Gender": "Male",
        "Last Login Time": "2:49 AM",
        "Salary": 69111,
        "Senior Management": "true",
        "Start Date": "Sat, 16 Feb 2008 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "19.28",
        "First Name": "James",
        "Gender": "Male",
        "Last Login Time": "5:19 PM",
        "Salary": 148985,
        "Senior Management": "false",
        "Start Date": "Fri, 15 Jan 1993 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "3.067",
        "First Name": "Jason",
        "Gender": "Male",
        "Last Login Time": "10:09 PM",
        "Salary": 78417,
        "Senior Management": "false",
        "Start Date": "Sun, 17 Oct 1999 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "6.22",
        "First Name": "Jason",
        "Gender": "Male",
        "Last Login Time": "2:54 PM",
        "Salary": 69244,
        "Senior Management": "true",
        "Start Date": "Fri, 20 Nov 1998 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "4.299",
        "First Name": "Jason",
        "Gender": "Male",
        "Last Login Time": "6:05 PM",
        "Salary": 75607,
        "Senior Management": "true",
        "Start Date": "Fri, 01 May 1998 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "9.34",
        "First Name": "Jerry",
        "Gender": "Male",
        "Last Login Time": "1:00 PM",
        "Salary": 138705,
        "Senior Management": "true",
        "Start Date": "Fri, 04 Mar 2005 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "19.096",
        "First Name": "Jerry",
        "Gender": "Male",
        "Last Login Time": "12:56 PM",
        "Salary": 95734,
        "Senior Management": "false",
        "Start Date": "Sat, 10 Jan 2004 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "9.177",
        "First Name": "Jerry",
        "Gender": "Male",
        "Last Login Time": "6:46 AM",
        "Salary": 140810,
        "Senior Management": "true",
        "Start Date": "Thu, 18 Dec 2003 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "18.845",
        "First Name": "Jerry",
        "Gender": "Male",
        "Last Login Time": "7:51 PM",
        "Salary": 121357,
        "Senior Management": "false",
        "Start Date": "Mon, 30 Jan 1995 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "11.393",
        "First Name": "Jerry",
        "Gender": "Male",
        "Last Login Time": "4:29 AM",
        "Salary": 98393,
        "Senior Management": "false",
        "Start Date": "Sun, 04 May 2003 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "18.855",
        "First Name": "Jerry",
        "Gender": "Male",
        "Last Login Time": "4:15 AM",
        "Salary": 140850,
        "Senior Management": "false",
        "Start Date": "Sun, 26 Mar 1989 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "9.653",
        "First Name": "Jesse",
        "Gender": "Male",
        "Last Login Time": "3:35 PM",
        "Salary": 118733,
        "Senior Management": "false",
        "Start Date": "Mon, 25 Oct 1999 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "3.873",
        "First Name": "Jesse",
        "Gender": "Male",
        "Last Login Time": "7:26 PM",
        "Salary": 79582,
        "Senior Management": "false",
        "Start Date": "Mon, 02 Mar 1981 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "5.413",
        "First Name": "Jimmy",
        "Gender": "Male",
        "Last Login Time": "5:53 PM",
        "Salary": 126310,
        "Senior Management": "true",
        "Start Date": "Tue, 07 Oct 1986 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "19.624",
        "First Name": "Jimmy",
        "Gender": "Male",
        "Last Login Time": "7:29 PM",
        "Salary": 63549,
        "Senior Management": "false",
        "Start Date": "Tue, 19 Nov 2013 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "19.467",
        "First Name": "Keith",
        "Gender": "Male",
        "Last Login Time": "3:02 PM",
        "Salary": 120672,
        "Senior Management": "false",
        "Start Date": "Wed, 12 Feb 2003 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "5.128",
        "First Name": "Kevin",
        "Gender": "Male",
        "Last Login Time": "7:31 AM",
        "Salary": 35061,
        "Senior Management": "false",
        "Start Date": "Thu, 25 Mar 1982 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "9.635",
        "First Name": "Kevin",
        "Gender": "Male",
        "Last Login Time": "2:07 AM",
        "Salary": 46080,
        "Senior Management": "false",
        "Start Date": "Sat, 12 Jul 1997 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "11.699",
        "First Name": "Kevin",
        "Gender": "Male",
        "Last Login Time": "8:26 PM",
        "Salary": 134598,
        "Senior Management": "false",
        "Start Date": "Tue, 23 Jun 1981 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "18.021",
        "First Name": "Kevin",
        "Gender": "Male",
        "Last Login Time": "6:59 PM",
        "Salary": 79906,
        "Senior Management": "true",
        "Start Date": "Thu, 20 Nov 1986 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "4.135",
        "First Name": "Kevin",
        "Gender": "Male",
        "Last Login Time": "3:22 PM",
        "Salary": 141498,
        "Senior Management": "true",
        "Start Date": "Fri, 01 Jul 2005 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "1.389",
        "First Name": "Larry",
        "Gender": "Male",
        "Last Login Time": "4:47 PM",
        "Salary": 101004,
        "Senior Management": "true",
        "Start Date": "Sat, 24 Jan 1998 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "5.14",
        "First Name": "Larry",
        "Gender": "Male",
        "Last Login Time": "1:00 PM",
        "Salary": 91133,
        "Senior Management": "false",
        "Start Date": "Wed, 27 Aug 2003 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "10.458",
        "First Name": "Larry",
        "Gender": "Male",
        "Last Login Time": "2:05 AM",
        "Salary": 97370,
        "Senior Management": "false",
        "Start Date": "Fri, 08 Jan 1999 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "11.985",
        "First Name": "Larry",
        "Gender": "Male",
        "Last Login Time": "4:45 PM",
        "Salary": 60500,
        "Senior Management": "false",
        "Start Date": "Sat, 20 Apr 2013 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "2.075",
        "First Name": "Louis",
        "Gender": "Male",
        "Last Login Time": "5:02 AM",
        "Salary": 95198,
        "Senior Management": "false",
        "Start Date": "Fri, 15 Apr 2011 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "9.146",
        "First Name": "Louis",
        "Gender": "Male",
        "Last Login Time": "5:19 PM",
        "Salary": 93022,
        "Senior Management": "true",
        "Start Date": "Tue, 16 Aug 2011 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "15.402",
        "First Name": "Peter",
        "Gender": "Male",
        "Last Login Time": "6:15 PM",
        "Salary": 84885,
        "Senior Management": "false",
        "Start Date": "Thu, 17 Nov 1994 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "8.411",
        "First Name": "Peter",
        "Gender": "Male",
        "Last Login Time": "9:09 AM",
        "Salary": 56580,
        "Senior Management": "true",
        "Start Date": "Sat, 22 Feb 2003 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "1.268",
        "First Name": "Peter",
        "Gender": "Male",
        "Last Login Time": "5:43 PM",
        "Salary": 69297,
        "Senior Management": "false",
        "Start Date": "Tue, 24 Nov 1992 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "13.132",
        "First Name": "Peter",
        "Gender": "Male",
        "Last Login Time": "7:28 AM",
        "Salary": 77933,
        "Senior Management": "true",
        "Start Date": "Mon, 22 Mar 1982 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "12.026",
        "First Name": "Peter",
        "Gender": "Male",
        "Last Login Time": "1:39 AM",
        "Salary": 102577,
        "Senior Management": "true",
        "Start Date": "Wed, 22 May 1991 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "4.232",
        "First Name": "Ralph",
        "Gender": "Male",
        "Last Login Time": "1:35 AM",
        "Salary": 71896,
        "Senior Management": "true",
        "Start Date": "Thu, 11 Nov 2004 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "4.03",
        "First Name": "Ralph",
        "Gender": "Male",
        "Last Login Time": "10:28 AM",
        "Salary": 106310,
        "Senior Management": "true",
        "Start Date": "Wed, 27 Oct 2010 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "8.4",
        "First Name": "Ralph",
        "Gender": "Male",
        "Last Login Time": "2:25 AM",
        "Salary": 81215,
        "Senior Management": "false",
        "Start Date": "Wed, 07 Mar 2012 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "16.248",
        "First Name": "Ralph",
        "Gender": "Male",
        "Last Login Time": "11:54 AM",
        "Salary": 50455,
        "Senior Management": "false",
        "Start Date": "Sun, 24 Mar 1996 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "7.227",
        "First Name": "Ralph",
        "Gender": "Male",
        "Last Login Time": "4:48 PM",
        "Salary": 89854,
        "Senior Management": "false",
        "Start Date": "Thu, 10 Feb 2000 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "1.952",
        "First Name": "Randy",
        "Gender": "Male",
        "Last Login Time": "12:12 PM",
        "Salary": 58129,
        "Senior Management": "true",
        "Start Date": "Sun, 14 Nov 1999 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "7.887",
        "First Name": "Randy",
        "Gender": "Male",
        "Last Login Time": "6:24 PM",
        "Salary": 135119,
        "Senior Management": "false",
        "Start Date": "Sun, 16 Mar 2014 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "14.842",
        "First Name": "Randy",
        "Gender": "Male",
        "Last Login Time": "7:39 PM",
        "Salary": 86723,
        "Senior Management": "false",
        "Start Date": "Thu, 02 May 2002 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "13.047",
        "First Name": "Randy",
        "Gender": "Male",
        "Last Login Time": "3:04 AM",
        "Salary": 89831,
        "Senior Management": "true",
        "Start Date": "Wed, 27 Sep 2000 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "14.077",
        "First Name": "Randy",
        "Gender": "Male",
        "Last Login Time": "5:33 AM",
        "Salary": 57266,
        "Senior Management": "false",
        "Start Date": "Sat, 25 Feb 2012 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "13.886",
        "First Name": "Roger",
        "Gender": "Male",
        "Last Login Time": "11:32 AM",
        "Salary": 88010,
        "Senior Management": "true",
        "Start Date": "Thu, 17 Apr 1980 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "6.46",
        "First Name": "Roger",
        "Gender": "Male",
        "Last Login Time": "3:55 PM",
        "Salary": 51430,
        "Senior Management": "false",
        "Start Date": "Fri, 19 Nov 2004 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "5.084",
        "First Name": "Roger",
        "Gender": "Male",
        "Last Login Time": "2:32 AM",
        "Salary": 140558,
        "Senior Management": "true",
        "Start Date": "Mon, 08 Nov 1982 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "4.887",
        "First Name": "Roger",
        "Gender": "Male",
        "Last Login Time": "4:56 PM",
        "Salary": 125033,
        "Senior Management": "true",
        "Start Date": "Mon, 03 Aug 2015 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "13.32",
        "First Name": "Roger",
        "Gender": "Male",
        "Last Login Time": "5:11 PM",
        "Salary": 105689,
        "Senior Management": "true",
        "Start Date": "Sat, 03 Jul 2010 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "15.343",
        "First Name": "Roger",
        "Gender": "Male",
        "Last Login Time": "10:04 PM",
        "Salary": 115582,
        "Senior Management": "true",
        "Start Date": "Mon, 02 May 1988 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "3.914",
        "First Name": "Scott",
        "Gender": "Male",
        "Last Login Time": "4:36 AM",
        "Salary": 58248,
        "Senior Management": "false",
        "Start Date": "Tue, 12 May 2009 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "4.45",
        "First Name": "Scott",
        "Gender": "Male",
        "Last Login Time": "3:45 AM",
        "Salary": 90429,
        "Senior Management": "false",
        "Start Date": "Sat, 17 Dec 2011 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "10.894",
        "First Name": "Scott",
        "Gender": "Male",
        "Last Login Time": "1:50 AM",
        "Salary": 64172,
        "Senior Management": "true",
        "Start Date": "Sat, 03 Aug 1996 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "1.965",
        "First Name": "Scott",
        "Gender": "Male",
        "Last Login Time": "2:47 PM",
        "Salary": 146812,
        "Senior Management": "true",
        "Start Date": "Sat, 17 Nov 2012 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "15.592",
        "First Name": "Scott",
        "Gender": "Male",
        "Last Login Time": "7:36 PM",
        "Salary": 96111,
        "Senior Management": "false",
        "Start Date": "Sat, 23 Nov 1996 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "8.226",
        "First Name": "Scott",
        "Gender": "Male",
        "Last Login Time": "8:08 AM",
        "Salary": 37385,
        "Senior Management": "true",
        "Start Date": "Sat, 20 Aug 2011 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "6.414",
        "First Name": "Shawn",
        "Gender": "Male",
        "Last Login Time": "7:45 PM",
        "Salary": 111737,
        "Senior Management": "false",
        "Start Date": "Sun, 07 Dec 1986 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "6.539",
        "First Name": "Shawn",
        "Gender": "Male",
        "Last Login Time": "2:55 AM",
        "Salary": 148115,
        "Senior Management": "true",
        "Start Date": "Fri, 23 Sep 2005 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "2.097",
        "First Name": "Shawn",
        "Gender": "Male",
        "Last Login Time": "10:24 AM",
        "Salary": 96610,
        "Senior Management": "true",
        "Start Date": "Thu, 03 Dec 2009 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "9.77",
        "First Name": "Shawn",
        "Gender": "Male",
        "Last Login Time": "10:11 PM",
        "Salary": 71975,
        "Senior Management": "false",
        "Start Date": "Tue, 29 Sep 1987 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "4.02",
        "First Name": "Shawn",
        "Gender": "Male",
        "Last Login Time": "3:05 AM",
        "Salary": 57871,
        "Senior Management": "true",
        "Start Date": "Fri, 29 Dec 2006 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "10.664",
        "First Name": "Shawn",
        "Gender": "Male",
        "Last Login Time": "2:12 PM",
        "Salary": 39335,
        "Senior Management": "false",
        "Start Date": "Mon, 17 Mar 2008 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "6.339",
        "First Name": "Shawn",
        "Gender": "Male",
        "Last Login Time": "5:36 PM",
        "Salary": 51667,
        "Senior Management": "false",
        "Start Date": "Thu, 13 Mar 2008 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "12.428",
        "First Name": "Steve",
        "Gender": "Male",
        "Last Login Time": "11:44 PM",
        "Salary": 61310,
        "Senior Management": "true",
        "Start Date": "Wed, 11 Nov 2009 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "9.54",
        "First Name": "Steve",
        "Gender": "Male",
        "Last Login Time": "6:58 AM",
        "Salary": 67780,
        "Senior Management": "true",
        "Start Date": "Tue, 22 Aug 1995 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "1.197",
        "First Name": "Steve",
        "Gender": "Male",
        "Last Login Time": "9:17 PM",
        "Salary": 51821,
        "Senior Management": "true",
        "Start Date": "Fri, 11 Jan 2002 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "13.464",
        "First Name": "Terry",
        "Gender": "Male",
        "Last Login Time": "6:30 PM",
        "Salary": 124008,
        "Senior Management": "true",
        "Start Date": "Fri, 27 Nov 1981 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "19.135",
        "First Name": "Terry",
        "Gender": "Male",
        "Last Login Time": "9:15 PM",
        "Salary": 52226,
        "Senior Management": "false",
        "Start Date": "Mon, 03 Sep 1990 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "7.969",
        "First Name": "Terry",
        "Gender": "Male",
        "Last Login Time": "11:18 PM",
        "Salary": 58357,
        "Senior Management": "false",
        "Start Date": "Thu, 21 Oct 2010 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "3.947",
        "First Name": "Terry",
        "Gender": "Male",
        "Last Login Time": "4:33 AM",
        "Salary": 35633,
        "Senior Management": "true",
        "Start Date": "Wed, 10 Nov 2004 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "14.085",
        "First Name": "Wayne",
        "Gender": "Male",
        "Last Login Time": "8:00 AM",
        "Salary": 102652,
        "Senior Management": "true",
        "Start Date": "Sat, 07 Apr 2012 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "17.066",
        "First Name": "Wayne",
        "Gender": "Male",
        "Last Login Time": "3:01 PM",
        "Salary": 81183,
        "Senior Management": "false",
        "Start Date": "Thu, 30 Jan 1992 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "18.396",
        "First Name": "Wayne",
        "Gender": "Male",
        "Last Login Time": "1:37 AM",
        "Salary": 126956,
        "Senior Management": "false",
        "Start Date": "Wed, 02 Sep 2009 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "2.728",
        "First Name": "Wayne",
        "Gender": "Male",
        "Last Login Time": "11:09 AM",
        "Salary": 67471,
        "Senior Management": "false",
        "Start Date": "Fri, 08 Sep 2006 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "19.717",
        "First Name": "Albert",
        "Gender": "Male",
        "Last Login Time": "4:20 PM",
        "Salary": 67827,
        "Senior Management": "true",
        "Start Date": "Sat, 01 Feb 1997 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "15.843",
        "First Name": "Albert",
        "Gender": "Male",
        "Last Login Time": "5:34 PM",
        "Salary": 102626,
        "Senior Management": "false",
        "Start Date": "Sun, 30 Sep 2007 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "9.705",
        "First Name": "Albert",
        "Gender": "Male",
        "Last Login Time": "5:43 PM",
        "Salary": 137840,
        "Senior Management": "false",
        "Start Date": "Thu, 14 Aug 2008 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "14.301",
        "First Name": "Albert",
        "Gender": "Male",
        "Last Login Time": "3:25 AM",
        "Salary": 86818,
        "Senior Management": "true",
        "Start Date": "Wed, 17 Jun 1992 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "5.85",
        "First Name": "Albert",
        "Gender": "Male",
        "Last Login Time": "2:35 AM",
        "Salary": 45094,
        "Senior Management": "true",
        "Start Date": "Sat, 19 Sep 1992 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "10.169",
        "First Name": "Albert",
        "Gender": "Male",
        "Last Login Time": "6:24 PM",
        "Salary": 129949,
        "Senior Management": "true",
        "Start Date": "Tue, 15 May 2012 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "7.563",
        "First Name": "Andrew",
        "Gender": "Male",
        "Last Login Time": "6:57 PM",
        "Salary": 43414,
        "Senior Management": "true",
        "Start Date": "Fri, 29 Mar 1985 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "8.611",
        "First Name": "Andrew",
        "Gender": "Male",
        "Last Login Time": "9:38 AM",
        "Salary": 137386,
        "Senior Management": "true",
        "Start Date": "Fri, 28 Sep 1990 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "14.422",
        "First Name": "Arthur",
        "Gender": "Male",
        "Last Login Time": "11:28 AM",
        "Salary": 89786,
        "Senior Management": "true",
        "Start Date": "Mon, 13 Apr 1998 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "6.147",
        "First Name": "Arthur",
        "Gender": "Male",
        "Last Login Time": "7:46 PM",
        "Salary": 134610,
        "Senior Management": "true",
        "Start Date": "Wed, 01 Jan 2014 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "6.639",
        "First Name": "Arthur",
        "Gender": "Male",
        "Last Login Time": "4:56 PM",
        "Salary": 66819,
        "Senior Management": "true",
        "Start Date": "Tue, 16 Dec 2014 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "3.412",
        "First Name": "Arthur",
        "Gender": "Male",
        "Last Login Time": "8:44 AM",
        "Salary": 86615,
        "Senior Management": "true",
        "Start Date": "Thu, 05 Dec 2013 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "10.763",
        "First Name": "Carlos",
        "Gender": "Male",
        "Last Login Time": "7:02 AM",
        "Salary": 146670,
        "Senior Management": "false",
        "Start Date": "Wed, 04 Jan 1995 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "11.58",
        "First Name": "Carlos",
        "Gender": "Male",
        "Last Login Time": "1:01 AM",
        "Salary": 77327,
        "Senior Management": "true",
        "Start Date": "Wed, 19 Sep 2007 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "2.362",
        "First Name": "Carlos",
        "Gender": "Male",
        "Last Login Time": "3:08 PM",
        "Salary": 50167,
        "Senior Management": "false",
        "Start Date": "Wed, 28 Jul 2010 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "14.737",
        "First Name": "Carlos",
        "Gender": "Male",
        "Last Login Time": "10:00 AM",
        "Salary": 138598,
        "Senior Management": "false",
        "Start Date": "Sun, 25 Jan 1981 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "15.866",
        "First Name": "Daniel",
        "Gender": "Male",
        "Last Login Time": "3:48 AM",
        "Salary": 106947,
        "Senior Management": "true",
        "Start Date": "Fri, 30 Apr 2010 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "7.664",
        "First Name": "Daniel",
        "Gender": "Male",
        "Last Login Time": "10:16 PM",
        "Salary": 123811,
        "Senior Management": "true",
        "Start Date": "Sat, 15 Sep 2007 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "13",
        "First Name": "Daniel",
        "Gender": "Male",
        "Last Login Time": "4:04 AM",
        "Salary": 77287,
        "Senior Management": "true",
        "Start Date": "Mon, 29 Feb 2016 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "10.125",
        "First Name": "Dennis",
        "Gender": "Male",
        "Last Login Time": "1:35 AM",
        "Salary": 115163,
        "Senior Management": "false",
        "Start Date": "Sat, 18 Apr 1987 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "6.499",
        "First Name": "Donald",
        "Gender": "Male",
        "Last Login Time": "7:51 AM",
        "Salary": 106472,
        "Senior Management": "true",
        "Start Date": "Fri, 14 Jul 1995 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "5.32",
        "First Name": "Donald",
        "Gender": "Male",
        "Last Login Time": "10:00 AM",
        "Salary": 122920,
        "Senior Management": "false",
        "Start Date": "Wed, 06 Apr 1988 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "6.466",
        "First Name": "Donald",
        "Gender": "Male",
        "Last Login Time": "2:25 AM",
        "Salary": 61999,
        "Senior Management": "false",
        "Start Date": "Thu, 01 Aug 1991 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "7.995",
        "First Name": "Edward",
        "Gender": "Male",
        "Last Login Time": "10:13 PM",
        "Salary": 110485,
        "Senior Management": "false",
        "Start Date": "Mon, 27 May 1985 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "10.957",
        "First Name": "Edward",
        "Gender": "Male",
        "Last Login Time": "6:06 AM",
        "Salary": 66067,
        "Senior Management": "true",
        "Start Date": "Fri, 04 Aug 1989 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "6.083",
        "First Name": "Edward",
        "Gender": "Male",
        "Last Login Time": "1:24 AM",
        "Salary": 73105,
        "Senior Management": "true",
        "Start Date": "Thu, 30 Aug 2001 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "17.095",
        "First Name": "Edward",
        "Gender": "Male",
        "Last Login Time": "1:00 AM",
        "Salary": 58327,
        "Senior Management": "true",
        "Start Date": "Thu, 27 Nov 1997 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "6.191",
        "First Name": "Ernest",
        "Gender": "Male",
        "Last Login Time": "11:25 AM",
        "Salary": 126232,
        "Senior Management": "true",
        "Start Date": "Tue, 14 Aug 2012 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "15.118",
        "First Name": "Ernest",
        "Gender": "Male",
        "Last Login Time": "12:08 AM",
        "Salary": 81919,
        "Senior Management": "false",
        "Start Date": "Sun, 28 Jan 1990 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "16.559",
        "First Name": "Ernest",
        "Gender": "Male",
        "Last Login Time": "1:46 PM",
        "Salary": 61181,
        "Senior Management": "false",
        "Start Date": "Sat, 30 Jun 2001 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "9.192",
        "First Name": "Ernest",
        "Gender": "Male",
        "Last Login Time": "2:02 PM",
        "Salary": 53335,
        "Senior Management": "false",
        "Start Date": "Sat, 06 Sep 1997 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "13.198",
        "First Name": "Ernest",
        "Gender": "Male",
        "Last Login Time": "6:41 AM",
        "Salary": 142935,
        "Senior Management": "true",
        "Start Date": "Sat, 20 Jul 2013 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "2.117",
        "First Name": "Eugene",
        "Gender": "Male",
        "Last Login Time": "10:54 AM",
        "Salary": 81077,
        "Senior Management": "false",
        "Start Date": "Thu, 24 May 1984 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "19.754",
        "First Name": "George",
        "Gender": "Male",
        "Last Login Time": "5:04 PM",
        "Salary": 36749,
        "Senior Management": "false",
        "Start Date": "Wed, 27 Sep 1995 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "18.9",
        "First Name": "George",
        "Gender": "Male",
        "Last Login Time": "5:40 AM",
        "Salary": 50369,
        "Senior Management": "true",
        "Start Date": "Fri, 05 Jun 2015 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "4.479",
        "First Name": "George",
        "Gender": "Male",
        "Last Login Time": "5:47 PM",
        "Salary": 98874,
        "Senior Management": "true",
        "Start Date": "Fri, 21 Jun 2013 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "1.923",
        "First Name": "Gerald",
        "Gender": "Male",
        "Last Login Time": "10:09 PM",
        "Salary": 121604,
        "Senior Management": "true",
        "Start Date": "Mon, 16 Apr 2001 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "9.331",
        "First Name": "Gerald",
        "Gender": "Male",
        "Last Login Time": "12:26 PM",
        "Salary": 96511,
        "Senior Management": "false",
        "Start Date": "Fri, 28 May 2010 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "2.469",
        "First Name": "Gerald",
        "Gender": "Male",
        "Last Login Time": "10:37 AM",
        "Salary": 96329,
        "Senior Management": "true",
        "Start Date": "Sat, 29 Mar 2003 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "12.447",
        "First Name": "Harold",
        "Gender": "Male",
        "Last Login Time": "9:40 PM",
        "Salary": 77544,
        "Senior Management": "false",
        "Start Date": "Wed, 02 Jan 1985 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "2.158",
        "First Name": "Harold",
        "Gender": "Male",
        "Last Login Time": "11:00 PM",
        "Salary": 66775,
        "Senior Management": "true",
        "Start Date": "Tue, 20 Feb 1990 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "1.187",
        "First Name": "Harold",
        "Gender": "Male",
        "Last Login Time": "8:45 PM",
        "Salary": 65673,
        "Senior Management": "true",
        "Start Date": "Mon, 18 Oct 2010 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "8.162",
        "First Name": "Harold",
        "Gender": "Male",
        "Last Login Time": "6:37 PM",
        "Salary": 118753,
        "Senior Management": "false",
        "Start Date": "Tue, 15 May 2007 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "11.626",
        "First Name": "Harold",
        "Gender": "Male",
        "Last Login Time": "5:13 AM",
        "Salary": 147417,
        "Senior Management": "true",
        "Start Date": "Fri, 16 Apr 2010 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "3.771",
        "First Name": "Harold",
        "Gender": "Male",
        "Last Login Time": "12:40 PM",
        "Salary": 140444,
        "Senior Management": "false",
        "Start Date": "Sat, 23 Jun 2012 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "1.563",
        "First Name": "Howard",
        "Gender": "Male",
        "Last Login Time": "1:10 AM",
        "Salary": 105062,
        "Senior Management": "false",
        "Start Date": "Mon, 27 Apr 1992 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "5.46",
        "First Name": "Howard",
        "Gender": "Male",
        "Last Login Time": "7:22 AM",
        "Salary": 97490,
        "Senior Management": "true",
        "Start Date": "Tue, 05 Oct 1982 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "2.021",
        "First Name": "Howard",
        "Gender": "Male",
        "Last Login Time": "6:36 AM",
        "Salary": 37984,
        "Senior Management": "false",
        "Start Date": "Mon, 09 Apr 2012 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "7.369",
        "First Name": "Jeremy",
        "Gender": "Male",
        "Last Login Time": "5:56 AM",
        "Salary": 90370,
        "Senior Management": "false",
        "Start Date": "Tue, 21 Sep 2010 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "3.887",
        "First Name": "Jeremy",
        "Gender": "Male",
        "Last Login Time": "8:50 AM",
        "Salary": 100238,
        "Senior Management": "true",
        "Start Date": "Fri, 01 Feb 2008 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "1.679",
        "First Name": "Jeremy",
        "Gender": "Male",
        "Last Login Time": "12:15 AM",
        "Salary": 49542,
        "Senior Management": "true",
        "Start Date": "Thu, 08 Jun 2000 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "13.657",
        "First Name": "Jeremy",
        "Gender": "Male",
        "Last Login Time": "6:20 PM",
        "Salary": 129460,
        "Senior Management": "true",
        "Start Date": "Tue, 14 Jun 1988 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "18.702",
        "First Name": "Jeremy",
        "Gender": "Male",
        "Last Login Time": "12:05 AM",
        "Salary": 46930,
        "Senior Management": "true",
        "Start Date": "Wed, 12 Aug 1981 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "19.276",
        "First Name": "Jeremy",
        "Gender": "Male",
        "Last Login Time": "6:24 AM",
        "Salary": 47885,
        "Senior Management": "true",
        "Start Date": "Sun, 29 May 1994 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "13.946",
        "First Name": "Jeremy",
        "Gender": "Male",
        "Last Login Time": "3:56 AM",
        "Salary": 43354,
        "Senior Management": "false",
        "Start Date": "Thu, 09 Aug 2001 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "12.2",
        "First Name": "Jeremy",
        "Gender": "Male",
        "Last Login Time": "8:22 AM",
        "Salary": 133033,
        "Senior Management": "false",
        "Start Date": "Wed, 26 Nov 1997 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "1.876",
        "First Name": "Jeremy",
        "Gender": "Male",
        "Last Login Time": "1:40 PM",
        "Salary": 131513,
        "Senior Management": "true",
        "Start Date": "Sun, 19 May 1991 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "16.194",
        "First Name": "Johnny",
        "Gender": "Male",
        "Last Login Time": "4:23 PM",
        "Salary": 118172,
        "Senior Management": "true",
        "Start Date": "Fri, 06 Nov 2009 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "5.861",
        "First Name": "Johnny",
        "Gender": "Male",
        "Last Login Time": "8:21 AM",
        "Salary": 115194,
        "Senior Management": "true",
        "Start Date": "Mon, 14 Sep 1992 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "5.437",
        "First Name": "Johnny",
        "Gender": "Male",
        "Last Login Time": "7:39 PM",
        "Salary": 76394,
        "Senior Management": "true",
        "Start Date": "Fri, 26 Feb 2016 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "12.986",
        "First Name": "Johnny",
        "Gender": "Male",
        "Last Login Time": "1:35 PM",
        "Salary": 91124,
        "Senior Management": "true",
        "Start Date": "Sun, 08 Jan 1995 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "2.097",
        "First Name": "Johnny",
        "Gender": "Male",
        "Last Login Time": "2:54 PM",
        "Salary": 71383,
        "Senior Management": "true",
        "Start Date": "Sun, 14 Jan 2007 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "3.672",
        "First Name": "Joseph",
        "Gender": "Male",
        "Last Login Time": "6:50 PM",
        "Salary": 102555,
        "Senior Management": "true",
        "Start Date": "Thu, 10 Sep 1992 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "12.737",
        "First Name": "Joseph",
        "Gender": "Male",
        "Last Login Time": "11:12 PM",
        "Salary": 107050,
        "Senior Management": "false",
        "Start Date": "Sun, 10 Oct 2010 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "19.601",
        "First Name": "Joseph",
        "Gender": "Male",
        "Last Login Time": "9:46 PM",
        "Salary": 126010,
        "Senior Management": "false",
        "Start Date": "Thu, 04 Nov 1982 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "15.804",
        "First Name": "Joseph",
        "Gender": "Male",
        "Last Login Time": "10:16 PM",
        "Salary": 139570,
        "Senior Management": "true",
        "Start Date": "Thu, 23 May 1985 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "9.555",
        "First Name": "Joshua",
        "Gender": "Male",
        "Last Login Time": "6:32 AM",
        "Salary": 72893,
        "Senior Management": "false",
        "Start Date": "Mon, 09 Nov 2009 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "8.047",
        "First Name": "Joshua",
        "Gender": "Male",
        "Last Login Time": "7:22 PM",
        "Salary": 68230,
        "Senior Management": "false",
        "Start Date": "Tue, 10 Jul 1984 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "5.197",
        "First Name": "Joshua",
        "Gender": "Male",
        "Last Login Time": "3:23 PM",
        "Salary": 95003,
        "Senior Management": "true",
        "Start Date": "Fri, 27 Jun 1997 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "4.366",
        "First Name": "Justin",
        "Gender": "Male",
        "Last Login Time": "5:58 PM",
        "Salary": 82782,
        "Senior Management": "true",
        "Start Date": "Sun, 06 Dec 1992 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "19.334",
        "First Name": "Justin",
        "Gender": "Male",
        "Last Login Time": "6:30 AM",
        "Salary": 121508,
        "Senior Management": "true",
        "Start Date": "Thu, 22 May 1986 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "3.459",
        "First Name": "Justin",
        "Gender": "Male",
        "Last Login Time": "10:30 AM",
        "Salary": 62454,
        "Senior Management": "true",
        "Start Date": "Mon, 06 Sep 1999 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "15.221",
        "First Name": "Justin",
        "Gender": "Male",
        "Last Login Time": "11:15 PM",
        "Salary": 78351,
        "Senior Management": "false",
        "Start Date": "Sun, 24 May 1981 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "18.824",
        "First Name": "Justin",
        "Gender": "Male",
        "Last Login Time": "11:00 PM",
        "Salary": 128036,
        "Senior Management": "false",
        "Start Date": "Sun, 10 Aug 1997 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "9.699",
        "First Name": "Justin",
        "Gender": "Male",
        "Last Login Time": "12:45 AM",
        "Salary": 112975,
        "Senior Management": "false",
        "Start Date": "Thu, 25 Jul 1991 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "2.844",
        "First Name": "Martin",
        "Gender": "Male",
        "Last Login Time": "6:29 PM",
        "Salary": 61117,
        "Senior Management": "false",
        "Start Date": "Thu, 25 Feb 2016 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "3.996",
        "First Name": "Philip",
        "Gender": "Male",
        "Last Login Time": "1:30 PM",
        "Salary": 89227,
        "Senior Management": "false",
        "Start Date": "Thu, 17 Jul 2008 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "19.897",
        "First Name": "Philip",
        "Gender": "Male",
        "Last Login Time": "11:21 AM",
        "Salary": 129968,
        "Senior Management": "false",
        "Start Date": "Wed, 02 Aug 1989 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "19.122",
        "First Name": "Philip",
        "Gender": "Male",
        "Last Login Time": "6:36 AM",
        "Salary": 122319,
        "Senior Management": "false",
        "Start Date": "Thu, 18 Jul 1985 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "16.014",
        "First Name": "Philip",
        "Gender": "Male",
        "Last Login Time": "10:56 AM",
        "Salary": 103557,
        "Senior Management": "true",
        "Start Date": "Fri, 11 Mar 2005 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "18.428",
        "First Name": "Robert",
        "Gender": "Male",
        "Last Login Time": "7:15 PM",
        "Salary": 38041,
        "Senior Management": "true",
        "Start Date": "Sat, 27 Oct 1990 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "19.93",
        "First Name": "Robert",
        "Gender": "Male",
        "Last Login Time": "5:00 AM",
        "Salary": 85799,
        "Senior Management": "false",
        "Start Date": "Tue, 18 Nov 2014 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "19.894",
        "First Name": "Robert",
        "Gender": "Male",
        "Last Login Time": "4:26 AM",
        "Salary": 123294,
        "Senior Management": "false",
        "Start Date": "Sat, 29 Oct 1994 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "19.944",
        "First Name": "Robert",
        "Gender": "Male",
        "Last Login Time": "11:20 AM",
        "Salary": 135882,
        "Senior Management": "false",
        "Start Date": "Sun, 11 Mar 2007 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "10.982",
        "First Name": "Robert",
        "Gender": "Male",
        "Last Login Time": "12:41 PM",
        "Salary": 111580,
        "Senior Management": "false",
        "Start Date": "Fri, 05 Nov 1982 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "12.757",
        "First Name": "Ronald",
        "Gender": "Male",
        "Last Login Time": "2:19 PM",
        "Salary": 121068,
        "Senior Management": "true",
        "Start Date": "Wed, 30 Apr 2014 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "4.99",
        "First Name": "Ronald",
        "Gender": "Male",
        "Last Login Time": "2:09 PM",
        "Salary": 96633,
        "Senior Management": "true",
        "Start Date": "Tue, 24 Feb 2009 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "18.536",
        "First Name": "Ronald",
        "Gender": "Male",
        "Last Login Time": "10:05 AM",
        "Salary": 50426,
        "Senior Management": "true",
        "Start Date": "Wed, 25 May 1983 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "5.319",
        "First Name": "Samuel",
        "Gender": "Male",
        "Last Login Time": "2:54 AM",
        "Salary": 76076,
        "Senior Management": "true",
        "Start Date": "Thu, 19 Dec 1991 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "11.593",
        "First Name": "Samuel",
        "Gender": "Male",
        "Last Login Time": "4:40 PM",
        "Salary": 85550,
        "Senior Management": "true",
        "Start Date": "Fri, 25 May 2012 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "3.787",
        "First Name": "Samuel",
        "Gender": "Male",
        "Last Login Time": "12:40 PM",
        "Salary": 43694,
        "Senior Management": "true",
        "Start Date": "Thu, 07 Aug 1997 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "8.379",
        "First Name": "Steven",
        "Gender": "Male",
        "Last Login Time": "9:20 PM",
        "Salary": 35095,
        "Senior Management": "true",
        "Start Date": "Sun, 30 Mar 1980 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "16.565",
        "First Name": "Steven",
        "Gender": "Male",
        "Last Login Time": "10:12 PM",
        "Salary": 68680,
        "Senior Management": "false",
        "Start Date": "Tue, 23 Apr 2013 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "9.494",
        "First Name": "Steven",
        "Gender": "Male",
        "Last Login Time": "3:03 PM",
        "Salary": 109095,
        "Senior Management": "false",
        "Start Date": "Wed, 01 Mar 1995 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "19.127",
        "First Name": "Steven",
        "Gender": "Male",
        "Last Login Time": "10:53 AM",
        "Salary": 62719,
        "Senior Management": "false",
        "Start Date": "Sun, 10 Nov 1985 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "2.846",
        "First Name": "Steven",
        "Gender": "Male",
        "Last Login Time": "2:14 PM",
        "Salary": 113060,
        "Senior Management": "true",
        "Start Date": "Tue, 12 May 2009 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "6.96",
        "First Name": "Steven",
        "Gender": "Male",
        "Last Login Time": "8:30 AM",
        "Salary": 83706,
        "Senior Management": "true",
        "Start Date": "Tue, 21 Nov 2006 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "18.892",
        "First Name": "Steven",
        "Gender": "Male",
        "Last Login Time": "12:32 AM",
        "Salary": 43252,
        "Senior Management": "false",
        "Start Date": "Sun, 07 Sep 1986 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "13.813",
        "First Name": "Steven",
        "Gender": "Male",
        "Last Login Time": "8:25 PM",
        "Salary": 100949,
        "Senior Management": "true",
        "Start Date": "Fri, 30 May 1980 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "16.843",
        "First Name": "Steven",
        "Gender": "Male",
        "Last Login Time": "4:55 AM",
        "Salary": 110306,
        "Senior Management": "true",
        "Start Date": "Sun, 05 Jul 2009 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "4.17",
        "First Name": "Thomas",
        "Gender": "Male",
        "Last Login Time": "6:53 AM",
        "Salary": 61933,
        "Senior Management": "true",
        "Start Date": "Sun, 31 Mar 1996 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "17.029",
        "First Name": "Thomas",
        "Gender": "Male",
        "Last Login Time": "2:24 PM",
        "Salary": 62096,
        "Senior Management": "false",
        "Start Date": "Sun, 04 Jun 1995 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "9.554",
        "First Name": "Thomas",
        "Gender": "Male",
        "Last Login Time": "1:04 PM",
        "Salary": 103235,
        "Senior Management": "true",
        "Start Date": "Wed, 06 Apr 2011 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "11.211",
        "First Name": "Thomas",
        "Gender": "Male",
        "Last Login Time": "9:51 AM",
        "Salary": 65251,
        "Senior Management": "false",
        "Start Date": "Sat, 07 Sep 1991 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "15.081",
        "First Name": "Thomas",
        "Gender": "Male",
        "Last Login Time": "9:29 AM",
        "Salary": 111371,
        "Senior Management": "true",
        "Start Date": "Thu, 03 May 1990 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "19.572",
        "First Name": "Thomas",
        "Gender": "Male",
        "Last Login Time": "3:10 PM",
        "Salary": 105681,
        "Senior Management": "false",
        "Start Date": "Sat, 12 Mar 2016 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "10.166",
        "First Name": "Victor",
        "Gender": "Male",
        "Last Login Time": "1:02 PM",
        "Salary": 124486,
        "Senior Management": "false",
        "Start Date": "Wed, 08 Jan 2003 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "17.138",
        "First Name": "Victor",
        "Gender": "Male",
        "Last Login Time": "7:44 AM",
        "Salary": 70817,
        "Senior Management": "false",
        "Start Date": "Thu, 11 Apr 1991 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "16.261",
        "First Name": "Victor",
        "Gender": "Male",
        "Last Login Time": "12:04 PM",
        "Salary": 123144,
        "Senior Management": "true",
        "Start Date": "Sat, 24 Sep 2005 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "3.942",
        "First Name": "Victor",
        "Gender": "Male",
        "Last Login Time": "5:01 PM",
        "Salary": 45267,
        "Senior Management": "true",
        "Start Date": "Wed, 10 Mar 2010 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "5.961",
        "First Name": "Walter",
        "Gender": "Male",
        "Last Login Time": "11:54 PM",
        "Salary": 127813,
        "Senior Management": "false",
        "Start Date": "Wed, 06 Jul 1983 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "5.461",
        "First Name": "Walter",
        "Gender": "Male",
        "Last Login Time": "1:59 PM",
        "Salary": 58789,
        "Senior Management": "false",
        "Start Date": "Sat, 04 Aug 2007 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "13.613",
        "First Name": "Walter",
        "Gender": "Male",
        "Last Login Time": "11:16 PM",
        "Salary": 125382,
        "Senior Management": "true",
        "Start Date": "Mon, 24 Sep 2007 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "16.323",
        "First Name": "Walter",
        "Gender": "Male",
        "Last Login Time": "12:39 AM",
        "Salary": 144701,
        "Senior Management": "true",
        "Start Date": "Thu, 21 May 1992 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "4.023",
        "First Name": "Willie",
        "Gender": "Male",
        "Last Login Time": "6:21 AM",
        "Salary": 64363,
        "Senior Management": "false",
        "Start Date": "Thu, 27 Nov 2003 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "1.451",
        "First Name": "Willie",
        "Gender": "Male",
        "Last Login Time": "8:20 PM",
        "Salary": 146651,
        "Senior Management": "true",
        "Start Date": "Tue, 17 Feb 1998 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "4.935",
        "First Name": "Willie",
        "Gender": "Male",
        "Last Login Time": "9:45 AM",
        "Salary": 55281,
        "Senior Management": "true",
        "Start Date": "Tue, 06 Jun 2006 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "19.691",
        "First Name": "Willie",
        "Gender": "Male",
        "Last Login Time": "1:03 PM",
        "Salary": 55038,
        "Senior Management": "false",
        "Start Date": "Sat, 22 Aug 2009 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "1.017",
        "First Name": "Willie",
        "Gender": "Male",
        "Last Login Time": "5:39 AM",
        "Salary": 141932,
        "Senior Management": "true",
        "Start Date": "Sat, 05 Dec 2009 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "3.645",
        "First Name": "Anthony",
        "Gender": "Male",
        "Last Login Time": "1:35 PM",
        "Salary": 146141,
        "Senior Management": "true",
        "Start Date": "Wed, 13 Feb 2013 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "14.837",
        "First Name": "Anthony",
        "Gender": "Male",
        "Last Login Time": "9:04 PM",
        "Salary": 96795,
        "Senior Management": "false",
        "Start Date": "Thu, 30 Jan 2014 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "11.625",
        "First Name": "Anthony",
        "Gender": "Male",
        "Last Login Time": "8:35 AM",
        "Salary": 112769,
        "Senior Management": "true",
        "Start Date": "Sun, 16 Oct 2011 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "13.101",
        "First Name": "Antonio",
        "Gender": "Male",
        "Last Login Time": "1:50 PM",
        "Salary": 60866,
        "Senior Management": "true",
        "Start Date": "Tue, 25 Oct 1988 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "5.478",
        "First Name": "Antonio",
        "Gender": "Male",
        "Last Login Time": "10:54 PM",
        "Salary": 41928,
        "Senior Management": "true",
        "Start Date": "Sun, 06 Jun 1999 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "5.266",
        "First Name": "Antonio",
        "Gender": "Male",
        "Last Login Time": "4:17 AM",
        "Salary": 137979,
        "Senior Management": "false",
        "Start Date": "Sun, 28 Dec 2003 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "17.492",
        "First Name": "Brandon",
        "Gender": "Male",
        "Last Login Time": "1:08 AM",
        "Salary": 112807,
        "Senior Management": "true",
        "Start Date": "Mon, 01 Dec 1980 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "8.012",
        "First Name": "Brandon",
        "Gender": "Male",
        "Last Login Time": "5:54 PM",
        "Salary": 115711,
        "Senior Management": "true",
        "Start Date": "Mon, 27 Mar 2006 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "4.664",
        "First Name": "Brandon",
        "Gender": "Male",
        "Last Login Time": "2:44 AM",
        "Salary": 112548,
        "Senior Management": "false",
        "Start Date": "Fri, 16 Oct 2015 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "2.709",
        "First Name": "Brandon",
        "Gender": "Male",
        "Last Login Time": "12:04 PM",
        "Salary": 60263,
        "Senior Management": "false",
        "Start Date": "Mon, 23 Oct 1995 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "1.26",
        "First Name": "Charles",
        "Gender": "Male",
        "Last Login Time": "8:13 PM",
        "Salary": 107391,
        "Senior Management": "true",
        "Start Date": "Tue, 14 Sep 2004 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "15.931",
        "First Name": "Charles",
        "Gender": "Male",
        "Last Login Time": "9:40 PM",
        "Salary": 71749,
        "Senior Management": "false",
        "Start Date": "Sat, 14 Oct 2000 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "7.077",
        "First Name": "Charles",
        "Gender": "Male",
        "Last Login Time": "8:28 PM",
        "Salary": 104014,
        "Senior Management": "false",
        "Start Date": "Thu, 16 Dec 1999 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "6.002",
        "First Name": "Charles",
        "Gender": "Male",
        "Last Login Time": "10:04 AM",
        "Salary": 148291,
        "Senior Management": "false",
        "Start Date": "Wed, 03 Sep 1997 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "6.945",
        "First Name": "Douglas",
        "Gender": "Male",
        "Last Login Time": "12:42 PM",
        "Salary": 97308,
        "Senior Management": "true",
        "Start Date": "Fri, 06 Aug 1993 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "1.015",
        "First Name": "Douglas",
        "Gender": "Male",
        "Last Login Time": "4:00 PM",
        "Salary": 83341,
        "Senior Management": "true",
        "Start Date": "Fri, 03 Sep 1999 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "14.372",
        "First Name": "Douglas",
        "Gender": "Male",
        "Last Login Time": "6:42 PM",
        "Salary": 41428,
        "Senior Management": "false",
        "Start Date": "Tue, 08 Jan 2002 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "2.28",
        "First Name": "Douglas",
        "Gender": "Male",
        "Last Login Time": "5:23 AM",
        "Salary": 132175,
        "Senior Management": "false",
        "Start Date": "Sat, 04 Aug 2007 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "3.845",
        "First Name": "Gregory",
        "Gender": "Male",
        "Last Login Time": "6:01 AM",
        "Salary": 109564,
        "Senior Management": "false",
        "Start Date": "Sat, 29 Jan 2000 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "11.204",
        "First Name": "Gregory",
        "Gender": "Male",
        "Last Login Time": "3:52 PM",
        "Salary": 142208,
        "Senior Management": "true",
        "Start Date": "Fri, 15 May 2009 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "16.304",
        "First Name": "Gregory",
        "Gender": "Male",
        "Last Login Time": "3:46 AM",
        "Salary": 82726,
        "Senior Management": "true",
        "Start Date": "Mon, 18 Jun 1984 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "15.857",
        "First Name": "Gregory",
        "Gender": "Male",
        "Last Login Time": "5:22 PM",
        "Salary": 128031,
        "Senior Management": "true",
        "Start Date": "Mon, 15 Nov 1999 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "12.075",
        "First Name": "Jeffrey",
        "Gender": "Male",
        "Last Login Time": "8:01 PM",
        "Salary": 45150,
        "Senior Management": "true",
        "Start Date": "Wed, 18 Jun 1997 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "2.673",
        "First Name": "Jeffrey",
        "Gender": "Male",
        "Last Login Time": "6:06 AM",
        "Salary": 111376,
        "Senior Management": "true",
        "Start Date": "Sat, 20 Sep 1986 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "15.901",
        "First Name": "Jeffrey",
        "Gender": "Male",
        "Last Login Time": "1:26 PM",
        "Salary": 70990,
        "Senior Management": "true",
        "Start Date": "Fri, 03 Feb 1984 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "16.439",
        "First Name": "Kenneth",
        "Gender": "Male",
        "Last Login Time": "9:16 PM",
        "Salary": 127654,
        "Senior Management": "true",
        "Start Date": "Tue, 25 Aug 1987 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "12.072",
        "First Name": "Kenneth",
        "Gender": "Male",
        "Last Login Time": "10:28 PM",
        "Salary": 81839,
        "Senior Management": "false",
        "Start Date": "Tue, 13 Apr 1999 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "17.862",
        "First Name": "Kenneth",
        "Gender": "Male",
        "Last Login Time": "6:55 AM",
        "Salary": 47232,
        "Senior Management": "true",
        "Start Date": "Sat, 14 Dec 1985 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "7.588",
        "First Name": "Kenneth",
        "Gender": "Male",
        "Last Login Time": "2:41 PM",
        "Salary": 69112,
        "Senior Management": "true",
        "Start Date": "Thu, 15 Jan 2015 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "1.905",
        "First Name": "Kenneth",
        "Gender": "Male",
        "Last Login Time": "8:24 AM",
        "Salary": 101914,
        "Senior Management": "true",
        "Start Date": "Wed, 10 May 2006 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "13.645",
        "First Name": "Matthew",
        "Gender": "Male",
        "Last Login Time": "2:12 AM",
        "Salary": 100612,
        "Senior Management": "false",
        "Start Date": "Tue, 05 Sep 1995 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "18.04",
        "First Name": "Matthew",
        "Gender": "Male",
        "Last Login Time": "10:33 PM",
        "Salary": 35203,
        "Senior Management": "false",
        "Start Date": "Wed, 02 Jan 2013 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "2.462",
        "First Name": "Matthew",
        "Gender": "Male",
        "Last Login Time": "8:04 AM",
        "Salary": 142373,
        "Senior Management": "false",
        "Start Date": "Wed, 31 Jul 2013 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "7.986",
        "First Name": "Matthew",
        "Gender": "Male",
        "Last Login Time": "5:39 AM",
        "Salary": 135352,
        "Senior Management": "true",
        "Start Date": "Thu, 03 Aug 1995 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "2.665",
        "First Name": "Michael",
        "Gender": "Male",
        "Last Login Time": "11:25 AM",
        "Salary": 99283,
        "Senior Management": "true",
        "Start Date": "Fri, 10 Oct 2008 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "12.659",
        "First Name": "Michael",
        "Gender": "Male",
        "Last Login Time": "3:04 AM",
        "Salary": 43586,
        "Senior Management": "false",
        "Start Date": "Thu, 24 Jan 2002 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "16.443",
        "First Name": "Michael",
        "Gender": "Male",
        "Last Login Time": "12:57 PM",
        "Salary": 98753,
        "Senior Management": "true",
        "Start Date": "Fri, 22 Nov 1991 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "18.357",
        "First Name": "Michael",
        "Gender": "Male",
        "Last Login Time": "10:42 AM",
        "Salary": 73354,
        "Senior Management": "false",
        "Start Date": "Sun, 22 May 2011 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "14.879",
        "First Name": "Michael",
        "Gender": "Male",
        "Last Login Time": "5:35 PM",
        "Salary": 35013,
        "Senior Management": "false",
        "Start Date": "Fri, 30 Jul 1993 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "2.617",
        "First Name": "Michael",
        "Gender": "Male",
        "Last Login Time": "1:48 PM",
        "Salary": 47079,
        "Senior Management": "false",
        "Start Date": "Wed, 13 Jul 1988 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "19.908",
        "First Name": "Michael",
        "Gender": "Male",
        "Last Login Time": "1:20 AM",
        "Salary": 81206,
        "Senior Management": "true",
        "Start Date": "Sat, 31 Aug 2002 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "17.495",
        "First Name": "Patrick",
        "Gender": "Male",
        "Last Login Time": "3:16 AM",
        "Salary": 143499,
        "Senior Management": "true",
        "Start Date": "Fri, 17 Aug 2007 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "5.368",
        "First Name": "Patrick",
        "Gender": "Male",
        "Last Login Time": "2:01 AM",
        "Salary": 75423,
        "Senior Management": "true",
        "Start Date": "Mon, 30 Dec 2002 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "14.66",
        "First Name": "Phillip",
        "Gender": "Male",
        "Last Login Time": "11:05 AM",
        "Salary": 36837,
        "Senior Management": "false",
        "Start Date": "Sun, 07 Oct 1984 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "6.842",
        "First Name": "Phillip",
        "Gender": "Male",
        "Last Login Time": "6:15 AM",
        "Salary": 134120,
        "Senior Management": "false",
        "Start Date": "Tue, 15 May 1984 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "19.675",
        "First Name": "Phillip",
        "Gender": "Male",
        "Last Login Time": "6:30 AM",
        "Salary": 42392,
        "Senior Management": "false",
        "Start Date": "Tue, 31 Jan 1984 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "3.178",
        "First Name": "Raymond",
        "Gender": "Male",
        "Last Login Time": "10:38 PM",
        "Salary": 37812,
        "Senior Management": "false",
        "Start Date": "Mon, 16 Feb 2009 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "16.69",
        "First Name": "Raymond",
        "Gender": "Male",
        "Last Login Time": "4:14 PM",
        "Salary": 114244,
        "Senior Management": "false",
        "Start Date": "Sat, 13 Jan 1996 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "2.712",
        "First Name": "Raymond",
        "Gender": "Male",
        "Last Login Time": "12:18 PM",
        "Salary": 47529,
        "Senior Management": "true",
        "Start Date": "Fri, 12 Dec 1986 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "10.717",
        "First Name": "Richard",
        "Gender": "Male",
        "Last Login Time": "1:41 AM",
        "Salary": 86326,
        "Senior Management": "false",
        "Start Date": "Tue, 27 Sep 2005 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "18.787",
        "First Name": "Richard",
        "Gender": "Male",
        "Last Login Time": "11:47 AM",
        "Salary": 47647,
        "Senior Management": "true",
        "Start Date": "Fri, 04 Jul 1997 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "17.885",
        "First Name": "Russell",
        "Gender": "Male",
        "Last Login Time": "1:48 AM",
        "Salary": 60388,
        "Senior Management": "false",
        "Start Date": "Sun, 02 Jan 2005 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "7.843",
        "First Name": "Russell",
        "Gender": "Male",
        "Last Login Time": "3:51 PM",
        "Salary": 121160,
        "Senior Management": "false",
        "Start Date": "Wed, 13 Aug 2014 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "9.669",
        "First Name": "Russell",
        "Gender": "Male",
        "Last Login Time": "5:46 AM",
        "Salary": 114334,
        "Senior Management": "false",
        "Start Date": "Sun, 30 Oct 1994 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "11.105",
        "First Name": "Russell",
        "Gender": "Male",
        "Last Login Time": "11:08 PM",
        "Salary": 137359,
        "Senior Management": "false",
        "Start Date": "Fri, 10 May 2013 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "1.421",
        "First Name": "Russell",
        "Gender": "Male",
        "Last Login Time": "12:39 PM",
        "Salary": 96914,
        "Senior Management": "false",
        "Start Date": "Mon, 20 May 2013 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "10.574",
        "First Name": "Stephen",
        "Gender": "Male",
        "Last Login Time": "12:47 PM",
        "Salary": 111249,
        "Senior Management": "true",
        "Start Date": "Thu, 09 Apr 1987 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "9.078",
        "First Name": "Stephen",
        "Gender": "Male",
        "Last Login Time": "7:07 PM",
        "Salary": 141958,
        "Senior Management": "true",
        "Start Date": "Sat, 09 May 2015 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "10.615",
        "First Name": "Stephen",
        "Gender": "Male",
        "Last Login Time": "6:26 AM",
        "Salary": 121816,
        "Senior Management": "true",
        "Start Date": "Sun, 21 Oct 1984 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "15.574",
        "First Name": "Stephen",
        "Gender": "Male",
        "Last Login Time": "10:42 PM",
        "Salary": 129663,
        "Senior Management": "false",
        "Start Date": "Mon, 10 Sep 1990 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "18.093",
        "First Name": "Stephen",
        "Gender": "Male",
        "Last Login Time": "11:34 PM",
        "Salary": 93997,
        "Senior Management": "true",
        "Start Date": "Sun, 29 Oct 1989 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "12.463",
        "First Name": "Timothy",
        "Gender": "Male",
        "Last Login Time": "10:49 PM",
        "Salary": 49473,
        "Senior Management": "false",
        "Start Date": "Wed, 06 Oct 2010 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "8.475",
        "First Name": "Timothy",
        "Gender": "Male",
        "Last Login Time": "10:37 AM",
        "Salary": 92587,
        "Senior Management": "false",
        "Start Date": "Sun, 25 Aug 1991 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "5.83",
        "First Name": "William",
        "Gender": "Male",
        "Last Login Time": "4:09 PM",
        "Salary": 66521,
        "Senior Management": "false",
        "Start Date": "Sun, 29 Sep 2002 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "5.182",
        "First Name": "William",
        "Gender": "Male",
        "Last Login Time": "12:27 PM",
        "Salary": 54058,
        "Senior Management": "true",
        "Start Date": "Thu, 18 Nov 1993 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "15.653",
        "First Name": "William",
        "Gender": "Male",
        "Last Login Time": "8:33 AM",
        "Salary": 104840,
        "Senior Management": "true",
        "Start Date": "Thu, 26 Jun 1997 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "7.008",
        "First Name": "Benjamin",
        "Gender": "Male",
        "Last Login Time": "10:06 PM",
        "Salary": 79529,
        "Senior Management": "true",
        "Start Date": "Wed, 26 Jan 2005 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "15.794",
        "First Name": "Benjamin",
        "Gender": "Male",
        "Last Login Time": "6:37 AM",
        "Salary": 84810,
        "Senior Management": "false",
        "Start Date": "Tue, 11 Sep 1984 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "7.123",
        "First Name": "Benjamin",
        "Gender": "Male",
        "Last Login Time": "3:28 PM",
        "Salary": 114356,
        "Senior Management": "false",
        "Start Date": "Sun, 05 May 2013 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "7.783",
        "First Name": "Benjamin",
        "Gender": "Male",
        "Last Login Time": "11:32 PM",
        "Salary": 123409,
        "Senior Management": "false",
        "Start Date": "Tue, 12 Apr 1988 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "6.083",
        "First Name": "Clarence",
        "Gender": "Male",
        "Last Login Time": "5:57 AM",
        "Salary": 93581,
        "Senior Management": "true",
        "Start Date": "Tue, 26 Mar 1996 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "1.215",
        "First Name": "Clarence",
        "Gender": "Male",
        "Last Login Time": "3:16 AM",
        "Salary": 85700,
        "Senior Management": "false",
        "Start Date": "Sat, 02 May 1998 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "8.866",
        "First Name": "Clarence",
        "Gender": "Male",
        "Last Login Time": "12:53 PM",
        "Salary": 142561,
        "Senior Management": "false",
        "Start Date": "Tue, 08 Oct 1996 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "13.835",
        "First Name": "Clarence",
        "Gender": "Male",
        "Last Login Time": "9:00 AM",
        "Salary": 116693,
        "Senior Management": "true",
        "Start Date": "Thu, 13 Jan 2005 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "8.457",
        "First Name": "Clarence",
        "Gender": "Male",
        "Last Login Time": "8:23 PM",
        "Salary": 124365,
        "Senior Management": "false",
        "Start Date": "Thu, 20 Aug 1992 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "18.654",
        "First Name": "Clarence",
        "Gender": "Male",
        "Last Login Time": "12:11 AM",
        "Salary": 103684,
        "Senior Management": "true",
        "Start Date": "Tue, 03 Nov 2015 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "4.905",
        "First Name": "Clarence",
        "Gender": "Male",
        "Last Login Time": "9:47 AM",
        "Salary": 146589,
        "Senior Management": "true",
        "Start Date": "Thu, 26 Aug 1982 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "11.517",
        "First Name": "Clarence",
        "Gender": "Male",
        "Last Login Time": "6:11 PM",
        "Salary": 148941,
        "Senior Management": "false",
        "Start Date": "Sat, 05 Aug 1989 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "16.736",
        "First Name": "Jonathan",
        "Gender": "Male",
        "Last Login Time": "8:15 AM",
        "Salary": 130581,
        "Senior Management": "true",
        "Start Date": "Fri, 17 Jul 2009 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "4.903",
        "First Name": "Jonathan",
        "Gender": "Male",
        "Last Login Time": "2:59 AM",
        "Salary": 141069,
        "Senior Management": "false",
        "Start Date": "Mon, 12 Oct 1987 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "11.364",
        "First Name": "Jonathan",
        "Gender": "Male",
        "Last Login Time": "12:01 AM",
        "Salary": 104749,
        "Senior Management": "false",
        "Start Date": "Thu, 15 Aug 2002 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "18.623",
        "First Name": "Jonathan",
        "Gender": "Male",
        "Last Login Time": "10:38 PM",
        "Salary": 56993,
        "Senior Management": "false",
        "Start Date": "Thu, 06 Apr 1995 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "12.922",
        "First Name": "Jonathan",
        "Gender": "Male",
        "Last Login Time": "6:02 PM",
        "Salary": 83809,
        "Senior Management": "false",
        "Start Date": "Mon, 30 Jul 1984 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "16.923",
        "First Name": "Jonathan",
        "Gender": "Male",
        "Last Login Time": "12:45 AM",
        "Salary": 121797,
        "Senior Management": "false",
        "Start Date": "Wed, 21 Aug 2013 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "18.641",
        "First Name": "Lawrence",
        "Gender": "Male",
        "Last Login Time": "1:25 AM",
        "Salary": 74640,
        "Senior Management": "false",
        "Start Date": "Fri, 13 May 2005 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "14.618",
        "First Name": "Lawrence",
        "Gender": "Male",
        "Last Login Time": "3:41 AM",
        "Salary": 122971,
        "Senior Management": "false",
        "Start Date": "Sat, 23 Jul 2011 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "9.127",
        "First Name": "Lawrence",
        "Gender": "Male",
        "Last Login Time": "10:55 PM",
        "Salary": 46378,
        "Senior Management": "false",
        "Start Date": "Mon, 03 Jul 1995 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "17.952",
        "First Name": "Lawrence",
        "Gender": "Male",
        "Last Login Time": "2:06 PM",
        "Salary": 102589,
        "Senior Management": "true",
        "Start Date": "Mon, 01 Oct 1984 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "1.113",
        "First Name": "Nicholas",
        "Gender": "Male",
        "Last Login Time": "8:21 PM",
        "Salary": 74669,
        "Senior Management": "true",
        "Start Date": "Tue, 12 Apr 1994 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "2.826",
        "First Name": "Nicholas",
        "Gender": "Male",
        "Last Login Time": "9:26 PM",
        "Salary": 101036,
        "Senior Management": "true",
        "Start Date": "Fri, 01 Mar 2013 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "14.822",
        "First Name": "Christopher",
        "Gender": "Male",
        "Last Login Time": "10:52 AM",
        "Salary": 47369,
        "Senior Management": "false",
        "Start Date": "Sun, 30 Mar 2008 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "11.449",
        "First Name": "Christopher",
        "Gender": "Male",
        "Last Login Time": "10:15 AM",
        "Salary": 37919,
        "Senior Management": "false",
        "Start Date": "Sat, 22 Apr 2000 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "17.984",
        "First Name": "Christopher",
        "Gender": "Male",
        "Last Login Time": "12:22 PM",
        "Salary": 142178,
        "Senior Management": "true",
        "Start Date": "Sat, 24 Dec 2011 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "7.869",
        "First Name": "Christopher",
        "Gender": "Male",
        "Last Login Time": "10:48 AM",
        "Salary": 68028,
        "Senior Management": "true",
        "Start Date": "Thu, 13 May 1999 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "7.252",
        "First Name": "Christopher",
        "Gender": "Male",
        "Last Login Time": "7:52 AM",
        "Salary": 82401,
        "Senior Management": "false",
        "Start Date": "Wed, 23 Apr 2014 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "11.598",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "10:43 AM",
        "Salary": 45906,
        "Senior Management": "null",
        "Start Date": "Mon, 20 Jul 2015 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "19.414",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "5:25 PM",
        "Salary": 58112,
        "Senior Management": "null",
        "Start Date": "Tue, 12 Jun 2007 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "10.527",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "1:08 AM",
        "Salary": 132373,
        "Senior Management": "null",
        "Start Date": "Wed, 03 Oct 1990 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "8.578",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "2:00 PM",
        "Salary": 86230,
        "Senior Management": "null",
        "Start Date": "Sun, 17 Aug 2014 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "14.443",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "8:32 AM",
        "Salary": 79536,
        "Senior Management": "null",
        "Start Date": "Wed, 27 Jul 2005 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "9.061",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "1:28 PM",
        "Salary": 59148,
        "Senior Management": "null",
        "Start Date": "Sun, 23 Mar 2014 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "7.014",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "6:52 PM",
        "Salary": 42341,
        "Senior Management": "null",
        "Start Date": "Tue, 09 Jul 1991 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "1.825",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "9:50 PM",
        "Salary": 149654,
        "Senior Management": "null",
        "Start Date": "Wed, 23 Feb 2005 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "5.56",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "12:49 PM",
        "Salary": 71945,
        "Senior Management": "null",
        "Start Date": "Mon, 17 Jun 1991 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "14.063",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "8:14 AM",
        "Salary": 115145,
        "Senior Management": "null",
        "Start Date": "Wed, 05 Aug 2009 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "18.517",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "8:35 PM",
        "Salary": 145316,
        "Senior Management": "null",
        "Start Date": "Sun, 02 Aug 1992 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "14.356",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "11:40 PM",
        "Salary": 62960,
        "Senior Management": "null",
        "Start Date": "Tue, 08 Jul 2008 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "3.171",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "11:02 PM",
        "Salary": 81444,
        "Senior Management": "null",
        "Start Date": "Sun, 31 Dec 2006 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "4.537",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "12:39 PM",
        "Salary": 118906,
        "Senior Management": "null",
        "Start Date": "Wed, 18 Sep 2002 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "12.182",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "3:57 PM",
        "Salary": 107024,
        "Senior Management": "null",
        "Start Date": "Thu, 18 Apr 1996 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "1.085",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "6:40 AM",
        "Salary": 93847,
        "Senior Management": "null",
        "Start Date": "Sat, 27 Apr 2013 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "3.099",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "8:01 PM",
        "Salary": 115436,
        "Senior Management": "null",
        "Start Date": "Sun, 26 Apr 1992 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "10.494",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "10:05 AM",
        "Salary": 38275,
        "Senior Management": "null",
        "Start Date": "Tue, 24 Jun 2014 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "4.82",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "3:30 AM",
        "Salary": 84746,
        "Senior Management": "null",
        "Start Date": "Wed, 02 Dec 2009 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "12.605",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "8:04 PM",
        "Salary": 48141,
        "Senior Management": "null",
        "Start Date": "Tue, 01 Apr 1980 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "7.421",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "1:01 PM",
        "Salary": 118736,
        "Senior Management": "null",
        "Start Date": "Tue, 13 Jan 2009 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "10.925",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "10:57 PM",
        "Salary": 98385,
        "Senior Management": "null",
        "Start Date": "Thu, 11 Oct 1990 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "17.274",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "5:17 PM",
        "Salary": 116236,
        "Senior Management": "null",
        "Start Date": "Sun, 24 Oct 1993 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "2.93",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "8:03 AM",
        "Salary": 131755,
        "Senior Management": "null",
        "Start Date": "Sun, 13 Apr 1997 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "1.4",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "8:42 PM",
        "Salary": 138807,
        "Senior Management": "null",
        "Start Date": "Sun, 18 Dec 1994 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "10.867",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "7:36 AM",
        "Salary": 106428,
        "Senior Management": "null",
        "Start Date": "Sun, 18 Jun 2000 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "8.941",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "12:00 AM",
        "Salary": 57811,
        "Senior Management": "null",
        "Start Date": "Sat, 24 Jul 1982 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "12.254",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "2:27 AM",
        "Salary": 80399,
        "Senior Management": "null",
        "Start Date": "Sat, 27 Dec 1980 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "19.388",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "4:19 PM",
        "Salary": 95866,
        "Senior Management": "null",
        "Start Date": "Wed, 23 Aug 2000 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "16.941",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "1:50 AM",
        "Salary": 133472,
        "Senior Management": "null",
        "Start Date": "Sun, 15 Sep 1985 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "9.662",
        "First Name": "null",
        "Gender": "Female",
        "Last Login Time": "5:19 AM",
        "Salary": 143638,
        "Senior Management": "null",
        "Start Date": "Tue, 14 Sep 2010 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "8.222",
        "First Name": "Amy",
        "Gender": "Female",
        "Last Login Time": "3:06 AM",
        "Salary": 122897,
        "Senior Management": "true",
        "Start Date": "Wed, 19 Jun 2002 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "15.967",
        "First Name": "Amy",
        "Gender": "Female",
        "Last Login Time": "10:54 PM",
        "Salary": 106249,
        "Senior Management": "false",
        "Start Date": "Sun, 30 Mar 2008 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "19.132",
        "First Name": "Amy",
        "Gender": "Female",
        "Last Login Time": "6:26 AM",
        "Salary": 75415,
        "Senior Management": "false",
        "Start Date": "Wed, 20 May 2009 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "6.22",
        "First Name": "Ann",
        "Gender": "Female",
        "Last Login Time": "12:17 PM",
        "Salary": 90719,
        "Senior Management": "false",
        "Start Date": "Sun, 04 Nov 1984 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "9.851",
        "First Name": "Ann",
        "Gender": "Female",
        "Last Login Time": "5:44 AM",
        "Salary": 79796,
        "Senior Management": "false",
        "Start Date": "Wed, 28 Sep 1994 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "12.772",
        "First Name": "Ann",
        "Gender": "Female",
        "Last Login Time": "9:27 AM",
        "Salary": 118431,
        "Senior Management": "true",
        "Start Date": "Mon, 16 Jul 2001 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "10.048",
        "First Name": "Ann",
        "Gender": "Female",
        "Last Login Time": "1:08 AM",
        "Salary": 96941,
        "Senior Management": "true",
        "Start Date": "Fri, 03 Oct 1980 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "5.272",
        "First Name": "Ann",
        "Gender": "Female",
        "Last Login Time": "6:37 AM",
        "Salary": 71958,
        "Senior Management": "true",
        "Start Date": "Fri, 28 Sep 2001 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "17.94",
        "First Name": "Ann",
        "Gender": "Female",
        "Last Login Time": "11:15 AM",
        "Salary": 89443,
        "Senior Management": "true",
        "Start Date": "Fri, 23 Sep 1994 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "2.366",
        "First Name": "Anna",
        "Gender": "Female",
        "Last Login Time": "2:34 PM",
        "Salary": 117293,
        "Senior Management": "false",
        "Start Date": "Tue, 15 Apr 2008 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "3.723",
        "First Name": "Anne",
        "Gender": "Female",
        "Last Login Time": "2:08 PM",
        "Salary": 69134,
        "Senior Management": "true",
        "Start Date": "Wed, 16 Jul 1986 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "18.284",
        "First Name": "Anne",
        "Gender": "Female",
        "Last Login Time": "6:45 AM",
        "Salary": 44537,
        "Senior Management": "true",
        "Start Date": "Tue, 07 Mar 2000 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "18.451",
        "First Name": "Anne",
        "Gender": "Female",
        "Last Login Time": "8:09 PM",
        "Salary": 71930,
        "Senior Management": "true",
        "Start Date": "Sat, 26 Oct 1996 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "16.636",
        "First Name": "Anne",
        "Gender": "Female",
        "Last Login Time": "12:30 PM",
        "Salary": 128305,
        "Senior Management": "false",
        "Start Date": "Wed, 21 Nov 1984 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "17.648",
        "First Name": "Jane",
        "Gender": "Female",
        "Last Login Time": "2:01 AM",
        "Salary": 144474,
        "Senior Management": "false",
        "Start Date": "Wed, 03 Sep 1997 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "18.115",
        "First Name": "Jane",
        "Gender": "Female",
        "Last Login Time": "8:39 AM",
        "Salary": 42424,
        "Senior Management": "false",
        "Start Date": "Wed, 01 Jun 1994 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "15.941",
        "First Name": "Jane",
        "Gender": "Female",
        "Last Login Time": "7:02 PM",
        "Salary": 128540,
        "Senior Management": "false",
        "Start Date": "Sat, 10 Jul 1999 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "13.623",
        "First Name": "Jane",
        "Gender": "Female",
        "Last Login Time": "1:23 PM",
        "Salary": 51923,
        "Senior Management": "false",
        "Start Date": "Sun, 12 Jan 1992 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "15.211",
        "First Name": "Jane",
        "Gender": "Female",
        "Last Login Time": "2:12 PM",
        "Salary": 59680,
        "Senior Management": "true",
        "Start Date": "Fri, 27 Apr 2012 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "16.18",
        "First Name": "Jean",
        "Gender": "Female",
        "Last Login Time": "9:07 AM",
        "Salary": 119082,
        "Senior Management": "false",
        "Start Date": "Sat, 18 Dec 1993 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "3.694",
        "First Name": "Joan",
        "Gender": "Female",
        "Last Login Time": "2:53 AM",
        "Salary": 120941,
        "Senior Management": "true",
        "Start Date": "Tue, 02 Oct 2007 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "2.304",
        "First Name": "Judy",
        "Gender": "Female",
        "Last Login Time": "12:10 AM",
        "Salary": 65931,
        "Senior Management": "false",
        "Start Date": "Tue, 16 Sep 1997 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "13.457",
        "First Name": "Judy",
        "Gender": "Female",
        "Last Login Time": "2:33 AM",
        "Salary": 109510,
        "Senior Management": "true",
        "Start Date": "Mon, 01 Jul 1991 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "5.668",
        "First Name": "Judy",
        "Gender": "Female",
        "Last Login Time": "3:32 PM",
        "Salary": 38092,
        "Senior Management": "false",
        "Start Date": "Thu, 01 Feb 1990 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "11.716",
        "First Name": "Judy",
        "Gender": "Female",
        "Last Login Time": "1:44 AM",
        "Salary": 48668,
        "Senior Management": "true",
        "Start Date": "Tue, 05 Apr 2011 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "1.821",
        "First Name": "Lisa",
        "Gender": "Female",
        "Last Login Time": "9:42 AM",
        "Salary": 115387,
        "Senior Management": "false",
        "Start Date": "Mon, 02 Nov 2009 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "10.28",
        "First Name": "Lisa",
        "Gender": "Female",
        "Last Login Time": "6:33 PM",
        "Salary": 38078,
        "Senior Management": "true",
        "Start Date": "Sat, 26 Feb 2005 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "17.108",
        "First Name": "Lisa",
        "Gender": "Female",
        "Last Login Time": "6:44 PM",
        "Salary": 113592,
        "Senior Management": "true",
        "Start Date": "Tue, 09 Feb 1982 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "2.03",
        "First Name": "Lisa",
        "Gender": "Female",
        "Last Login Time": "1:04 AM",
        "Salary": 128042,
        "Senior Management": "true",
        "Start Date": "Wed, 11 Apr 2007 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "6.293",
        "First Name": "Lisa",
        "Gender": "Female",
        "Last Login Time": "9:19 PM",
        "Salary": 40121,
        "Senior Management": "false",
        "Start Date": "Sat, 08 Jul 2000 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "18.53",
        "First Name": "Lisa",
        "Gender": "Female",
        "Last Login Time": "1:42 PM",
        "Salary": 73706,
        "Senior Management": "false",
        "Start Date": "Fri, 17 Oct 2003 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "2.235",
        "First Name": "Lois",
        "Gender": "Female",
        "Last Login Time": "4:16 PM",
        "Salary": 106317,
        "Senior Management": "true",
        "Start Date": "Fri, 25 Dec 1987 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "6.652",
        "First Name": "Lois",
        "Gender": "Female",
        "Last Login Time": "4:51 PM",
        "Salary": 36946,
        "Senior Management": "false",
        "Start Date": "Fri, 18 Oct 2013 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "9.999",
        "First Name": "Lois",
        "Gender": "Female",
        "Last Login Time": "7:06 AM",
        "Salary": 147183,
        "Senior Management": "true",
        "Start Date": "Wed, 09 Nov 2011 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "19.075",
        "First Name": "Lois",
        "Gender": "Female",
        "Last Login Time": "11:39 AM",
        "Salary": 53954,
        "Senior Management": "false",
        "Start Date": "Sat, 28 Jul 2012 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "6.168",
        "First Name": "Lois",
        "Gender": "Female",
        "Last Login Time": "4:10 PM",
        "Salary": 99747,
        "Senior Management": "false",
        "Start Date": "Fri, 11 Dec 2015 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "14.223",
        "First Name": "Lori",
        "Gender": "Female",
        "Last Login Time": "10:59 PM",
        "Salary": 95389,
        "Senior Management": "false",
        "Start Date": "Thu, 31 Mar 1988 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "3.345",
        "First Name": "Lori",
        "Gender": "Female",
        "Last Login Time": "7:36 AM",
        "Salary": 66029,
        "Senior Management": "true",
        "Start Date": "Wed, 11 Sep 2002 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "6.537",
        "First Name": "Lori",
        "Gender": "Female",
        "Last Login Time": "1:15 PM",
        "Salary": 75498,
        "Senior Management": "true",
        "Start Date": "Fri, 20 Nov 2015 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "18.197",
        "First Name": "Mary",
        "Gender": "Female",
        "Last Login Time": "1:03 AM",
        "Salary": 134645,
        "Senior Management": "false",
        "Start Date": "Fri, 13 Aug 1999 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "3.8",
        "First Name": "Mary",
        "Gender": "Female",
        "Last Login Time": "11:41 PM",
        "Salary": 92544,
        "Senior Management": "false",
        "Start Date": "Sat, 30 May 2009 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "12.484",
        "First Name": "Mary",
        "Gender": "Female",
        "Last Login Time": "6:32 PM",
        "Salary": 87721,
        "Senior Management": "false",
        "Start Date": "Sun, 18 Oct 2009 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "17.538",
        "First Name": "Mary",
        "Gender": "Female",
        "Last Login Time": "8:03 AM",
        "Salary": 42214,
        "Senior Management": "true",
        "Start Date": "Sun, 22 Aug 2010 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "2.089",
        "First Name": "Mary",
        "Gender": "Female",
        "Last Login Time": "8:32 AM",
        "Salary": 115057,
        "Senior Management": "false",
        "Start Date": "Sun, 06 Nov 2011 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "19.385",
        "First Name": "Rose",
        "Gender": "Female",
        "Last Login Time": "3:57 PM",
        "Salary": 63494,
        "Senior Management": "true",
        "Start Date": "Sat, 06 Jul 2002 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "5.63",
        "First Name": "Rose",
        "Gender": "Female",
        "Last Login Time": "8:40 AM",
        "Salary": 149903,
        "Senior Management": "false",
        "Start Date": "Thu, 28 May 2015 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "7.585",
        "First Name": "Rose",
        "Gender": "Female",
        "Last Login Time": "4:34 PM",
        "Salary": 56961,
        "Senior Management": "false",
        "Start Date": "Sat, 30 Oct 2004 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "2.142",
        "First Name": "Rose",
        "Gender": "Female",
        "Last Login Time": "9:14 AM",
        "Salary": 97691,
        "Senior Management": "false",
        "Start Date": "Thu, 20 May 1982 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "6.06",
        "First Name": "Rose",
        "Gender": "Female",
        "Last Login Time": "9:06 AM",
        "Salary": 75181,
        "Senior Management": "true",
        "Start Date": "Wed, 03 Nov 1999 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "19.85",
        "First Name": "Rose",
        "Gender": "Female",
        "Last Login Time": "6:50 PM",
        "Salary": 145001,
        "Senior Management": "false",
        "Start Date": "Fri, 31 Dec 1982 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "9.828",
        "First Name": "Rose",
        "Gender": "Female",
        "Last Login Time": "9:14 PM",
        "Salary": 49538,
        "Senior Management": "false",
        "Start Date": "Wed, 02 Jan 2002 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "8.639",
        "First Name": "Rose",
        "Gender": "Female",
        "Last Login Time": "10:43 AM",
        "Salary": 91411,
        "Senior Management": "true",
        "Start Date": "Tue, 06 Apr 1982 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "11.051",
        "First Name": "Rose",
        "Gender": "Female",
        "Last Login Time": "5:12 AM",
        "Salary": 134505,
        "Senior Management": "true",
        "Start Date": "Sun, 25 Aug 2002 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "10.012",
        "First Name": "Ruby",
        "Gender": "Female",
        "Last Login Time": "4:20 PM",
        "Salary": 65476,
        "Senior Management": "true",
        "Start Date": "Mon, 17 Aug 1987 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "1.139",
        "First Name": "Ruby",
        "Gender": "Female",
        "Last Login Time": "7:35 PM",
        "Salary": 105946,
        "Senior Management": "false",
        "Start Date": "Wed, 08 Nov 2000 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "6.031",
        "First Name": "Ruby",
        "Gender": "Female",
        "Last Login Time": "8:27 PM",
        "Salary": 76707,
        "Senior Management": "false",
        "Start Date": "Sat, 10 Dec 1988 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "7.851",
        "First Name": "Ruby",
        "Gender": "Female",
        "Last Login Time": "3:36 AM",
        "Salary": 147362,
        "Senior Management": "true",
        "Start Date": "Sat, 01 May 1999 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "6.773",
        "First Name": "Ruby",
        "Gender": "Female",
        "Last Login Time": "3:42 AM",
        "Salary": 101262,
        "Senior Management": "false",
        "Start Date": "Mon, 07 Jul 1980 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "4.083",
        "First Name": "Ruby",
        "Gender": "Female",
        "Last Login Time": "8:41 PM",
        "Salary": 83112,
        "Senior Management": "false",
        "Start Date": "Sat, 31 May 2008 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "19.501",
        "First Name": "Ruby",
        "Gender": "Female",
        "Last Login Time": "6:27 PM",
        "Salary": 48354,
        "Senior Management": "false",
        "Start Date": "Sun, 13 Aug 2006 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "6.318",
        "First Name": "Ruby",
        "Gender": "Female",
        "Last Login Time": "11:08 PM",
        "Salary": 142868,
        "Senior Management": "false",
        "Start Date": "Mon, 28 Jan 1980 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "8.067",
        "First Name": "Ruth",
        "Gender": "Female",
        "Last Login Time": "4:03 AM",
        "Salary": 129297,
        "Senior Management": "true",
        "Start Date": "Thu, 19 Aug 1999 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "9.148",
        "First Name": "Ruth",
        "Gender": "Female",
        "Last Login Time": "7:29 PM",
        "Salary": 44639,
        "Senior Management": "true",
        "Start Date": "Tue, 12 Aug 1986 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "18.029",
        "First Name": "Ruth",
        "Gender": "Female",
        "Last Login Time": "4:13 AM",
        "Salary": 69579,
        "Senior Management": "true",
        "Start Date": "Tue, 24 Oct 2000 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "3.997",
        "First Name": "Ruth",
        "Gender": "Female",
        "Last Login Time": "10:07 AM",
        "Salary": 97915,
        "Senior Management": "true",
        "Start Date": "Thu, 12 Dec 1996 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "14.064",
        "First Name": "Ruth",
        "Gender": "Female",
        "Last Login Time": "5:38 AM",
        "Salary": 59969,
        "Senior Management": "true",
        "Start Date": "Tue, 17 Feb 2004 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "10.895",
        "First Name": "Ruth",
        "Gender": "Female",
        "Last Login Time": "6:52 AM",
        "Salary": 59678,
        "Senior Management": "false",
        "Start Date": "Tue, 02 Sep 1980 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "8.999",
        "First Name": "Sara",
        "Gender": "Female",
        "Last Login Time": "9:23 AM",
        "Salary": 83677,
        "Senior Management": "false",
        "Start Date": "Wed, 15 Aug 2007 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "9.402",
        "First Name": "Sara",
        "Gender": "Female",
        "Last Login Time": "6:17 PM",
        "Salary": 97058,
        "Senior Management": "false",
        "Start Date": "Mon, 23 Sep 1991 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "3.186",
        "First Name": "Sara",
        "Gender": "Female",
        "Last Login Time": "10:50 PM",
        "Salary": 75484,
        "Senior Management": "false",
        "Start Date": "Mon, 25 Feb 1980 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "16.961",
        "First Name": "Tina",
        "Gender": "Female",
        "Last Login Time": "7:47 PM",
        "Salary": 100705,
        "Senior Management": "true",
        "Start Date": "Thu, 16 Jun 2016 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "3.711",
        "First Name": "Tina",
        "Gender": "Female",
        "Last Login Time": "7:16 AM",
        "Salary": 114767,
        "Senior Management": "true",
        "Start Date": "Fri, 12 Jun 2009 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "14.248",
        "First Name": "Tina",
        "Gender": "Female",
        "Last Login Time": "9:11 AM",
        "Salary": 88276,
        "Senior Management": "false",
        "Start Date": "Mon, 17 Jan 2005 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "3.369",
        "First Name": "Tina",
        "Gender": "Female",
        "Last Login Time": "3:18 AM",
        "Salary": 102841,
        "Senior Management": "false",
        "Start Date": "Fri, 06 Aug 1999 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "19.04",
        "First Name": "Tina",
        "Gender": "Female",
        "Last Login Time": "3:53 PM",
        "Salary": 56450,
        "Senior Management": "true",
        "Start Date": "Thu, 15 May 1997 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "2.378",
        "First Name": "Alice",
        "Gender": "Female",
        "Last Login Time": "1:50 AM",
        "Salary": 51395,
        "Senior Management": "true",
        "Start Date": "Fri, 02 May 1986 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "10.485",
        "First Name": "Alice",
        "Gender": "Female",
        "Last Login Time": "5:07 PM",
        "Salary": 117787,
        "Senior Management": "false",
        "Start Date": "Thu, 21 Jan 2016 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "2.782",
        "First Name": "Alice",
        "Gender": "Female",
        "Last Login Time": "9:19 PM",
        "Salary": 92799,
        "Senior Management": "false",
        "Start Date": "Mon, 16 Oct 1995 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "4.363",
        "First Name": "Alice",
        "Gender": "Female",
        "Last Login Time": "12:49 AM",
        "Salary": 121250,
        "Senior Management": "true",
        "Start Date": "Sat, 09 Feb 2013 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "12.09",
        "First Name": "Alice",
        "Gender": "Female",
        "Last Login Time": "3:09 AM",
        "Salary": 131952,
        "Senior Management": "false",
        "Start Date": "Sat, 23 Mar 1996 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "15.397",
        "First Name": "Alice",
        "Gender": "Female",
        "Last Login Time": "8:54 PM",
        "Salary": 63571,
        "Senior Management": "true",
        "Start Date": "Sat, 03 Sep 1988 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "11.209",
        "First Name": "Alice",
        "Gender": "Female",
        "Last Login Time": "9:34 AM",
        "Salary": 47638,
        "Senior Management": "false",
        "Start Date": "Tue, 05 Oct 2004 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "8.276",
        "First Name": "Annie",
        "Gender": "Female",
        "Last Login Time": "2:05 AM",
        "Salary": 144887,
        "Senior Management": "true",
        "Start Date": "Sat, 30 Jan 1993 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "4.338",
        "First Name": "Annie",
        "Gender": "Female",
        "Last Login Time": "6:19 AM",
        "Salary": 40119,
        "Senior Management": "true",
        "Start Date": "Mon, 19 Dec 1994 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "9.801",
        "First Name": "Annie",
        "Gender": "Female",
        "Last Login Time": "10:04 AM",
        "Salary": 138925,
        "Senior Management": "true",
        "Start Date": "Sat, 06 Jun 1992 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "19.55",
        "First Name": "Betty",
        "Gender": "Female",
        "Last Login Time": "3:59 AM",
        "Salary": 104896,
        "Senior Management": "true",
        "Start Date": "Wed, 12 Jun 2002 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "12.984",
        "First Name": "Betty",
        "Gender": "Female",
        "Last Login Time": "6:03 PM",
        "Salary": 51613,
        "Senior Management": "false",
        "Start Date": "Tue, 28 Jun 2005 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "7.645",
        "First Name": "Betty",
        "Gender": "Female",
        "Last Login Time": "10:40 AM",
        "Salary": 37005,
        "Senior Management": "true",
        "Start Date": "Tue, 19 Nov 2002 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "9.129",
        "First Name": "Carol",
        "Gender": "Female",
        "Last Login Time": "3:39 AM",
        "Salary": 57783,
        "Senior Management": "false",
        "Start Date": "Tue, 19 Mar 1996 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "4.75",
        "First Name": "Debra",
        "Gender": "Female",
        "Last Login Time": "11:16 PM",
        "Salary": 48696,
        "Senior Management": "false",
        "Start Date": "Fri, 13 Mar 1998 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "18.456",
        "First Name": "Debra",
        "Gender": "Female",
        "Last Login Time": "10:25 PM",
        "Salary": 104250,
        "Senior Management": "true",
        "Start Date": "Tue, 22 Feb 1994 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "8.895",
        "First Name": "Debra",
        "Gender": "Female",
        "Last Login Time": "8:48 AM",
        "Salary": 70492,
        "Senior Management": "false",
        "Start Date": "Tue, 19 Jan 2010 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "19.513",
        "First Name": "Debra",
        "Gender": "Female",
        "Last Login Time": "12:19 PM",
        "Salary": 74911,
        "Senior Management": "false",
        "Start Date": "Sat, 12 Mar 1983 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "16.922",
        "First Name": "Debra",
        "Gender": "Female",
        "Last Login Time": "6:51 AM",
        "Salary": 42296,
        "Senior Management": "false",
        "Start Date": "Sun, 28 May 2006 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "6.976",
        "First Name": "Debra",
        "Gender": "Female",
        "Last Login Time": "1:12 PM",
        "Salary": 84693,
        "Senior Management": "true",
        "Start Date": "Thu, 17 Mar 2011 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "19.082",
        "First Name": "Diana",
        "Gender": "Female",
        "Last Login Time": "10:27 AM",
        "Salary": 132940,
        "Senior Management": "false",
        "Start Date": "Fri, 23 Oct 1981 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "2.784",
        "First Name": "Diana",
        "Gender": "Female",
        "Last Login Time": "7:53 AM",
        "Salary": 103521,
        "Senior Management": "true",
        "Start Date": "Fri, 04 Jan 2013 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "4.548",
        "First Name": "Diana",
        "Gender": "Female",
        "Last Login Time": "4:21 PM",
        "Salary": 41831,
        "Senior Management": "false",
        "Start Date": "Mon, 13 Jun 1994 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "18.003",
        "First Name": "Diana",
        "Gender": "Female",
        "Last Login Time": "12:37 AM",
        "Salary": 86883,
        "Senior Management": "true",
        "Start Date": "Thu, 19 Jan 1995 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "17.343",
        "First Name": "Diana",
        "Gender": "Female",
        "Last Login Time": "8:47 AM",
        "Salary": 105066,
        "Senior Management": "true",
        "Start Date": "Fri, 19 Nov 2004 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "17.018",
        "First Name": "Diane",
        "Gender": "Female",
        "Last Login Time": "3:22 AM",
        "Salary": 64084,
        "Senior Management": "false",
        "Start Date": "Sun, 18 Apr 1993 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "15.026",
        "First Name": "Diane",
        "Gender": "Female",
        "Last Login Time": "4:56 PM",
        "Salary": 124889,
        "Senior Management": "true",
        "Start Date": "Mon, 05 Jul 1982 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "13.506",
        "First Name": "Diane",
        "Gender": "Female",
        "Last Login Time": "6:14 PM",
        "Salary": 49501,
        "Senior Management": "false",
        "Start Date": "Tue, 02 Feb 1988 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "12.791",
        "First Name": "Diane",
        "Gender": "Female",
        "Last Login Time": "6:56 PM",
        "Salary": 130577,
        "Senior Management": "false",
        "Start Date": "Fri, 30 Oct 2009 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "1.894",
        "First Name": "Donna",
        "Gender": "Female",
        "Last Login Time": "3:48 AM",
        "Salary": 81014,
        "Senior Management": "false",
        "Start Date": "Thu, 22 Jul 2010 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "6.155",
        "First Name": "Donna",
        "Gender": "Female",
        "Last Login Time": "1:59 PM",
        "Salary": 64088,
        "Senior Management": "true",
        "Start Date": "Wed, 27 Nov 1991 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "17.999",
        "First Name": "Donna",
        "Gender": "Female",
        "Last Login Time": "7:04 AM",
        "Salary": 82871,
        "Senior Management": "false",
        "Start Date": "Fri, 26 Nov 1982 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "7.511",
        "First Name": "Doris",
        "Gender": "Female",
        "Last Login Time": "5:51 AM",
        "Salary": 83072,
        "Senior Management": "false",
        "Start Date": "Fri, 20 Aug 2004 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "7.425",
        "First Name": "Doris",
        "Gender": "Female",
        "Last Login Time": "6:40 PM",
        "Salary": 85215,
        "Senior Management": "true",
        "Start Date": "Wed, 29 Jul 1992 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "17.799",
        "First Name": "Doris",
        "Gender": "Female",
        "Last Login Time": "7:03 PM",
        "Salary": 114360,
        "Senior Management": "true",
        "Start Date": "Sat, 08 Sep 1984 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "3.799",
        "First Name": "Doris",
        "Gender": "Female",
        "Last Login Time": "5:54 PM",
        "Salary": 141439,
        "Senior Management": "false",
        "Start Date": "Mon, 05 Jul 1993 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "11.295",
        "First Name": "Emily",
        "Gender": "Female",
        "Last Login Time": "11:25 AM",
        "Salary": 89434,
        "Senior Management": "false",
        "Start Date": "Thu, 20 Sep 2007 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "19.028",
        "First Name": "Emily",
        "Gender": "Female",
        "Last Login Time": "6:42 AM",
        "Salary": 36711,
        "Senior Management": "true",
        "Start Date": "Wed, 13 Jan 1988 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "14.841",
        "First Name": "Helen",
        "Gender": "Female",
        "Last Login Time": "2:30 AM",
        "Salary": 73789,
        "Senior Management": "true",
        "Start Date": "Thu, 29 Nov 2001 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "4.188",
        "First Name": "Helen",
        "Gender": "Female",
        "Last Login Time": "2:43 AM",
        "Salary": 52875,
        "Senior Management": "false",
        "Start Date": "Fri, 31 Oct 1997 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "11.279",
        "First Name": "Irene",
        "Gender": "Female",
        "Last Login Time": "9:32 AM",
        "Salary": 66851,
        "Senior Management": "false",
        "Start Date": "Wed, 07 May 1997 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "19.02",
        "First Name": "Irene",
        "Gender": "Female",
        "Last Login Time": "11:36 AM",
        "Salary": 133772,
        "Senior Management": "true",
        "Start Date": "Wed, 29 Jan 1992 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "8.996",
        "First Name": "Irene",
        "Gender": "Female",
        "Last Login Time": "8:25 PM",
        "Salary": 131038,
        "Senior Management": "false",
        "Start Date": "Fri, 30 Jan 2004 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "12.182",
        "First Name": "Irene",
        "Gender": "Female",
        "Last Login Time": "5:26 PM",
        "Salary": 40837,
        "Senior Management": "true",
        "Start Date": "Thu, 04 Feb 1982 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "5.81",
        "First Name": "Irene",
        "Gender": "Female",
        "Last Login Time": "8:26 AM",
        "Salary": 56526,
        "Senior Management": "true",
        "Start Date": "Wed, 03 Mar 1982 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "8.999",
        "First Name": "Irene",
        "Gender": "Female",
        "Last Login Time": "11:03 AM",
        "Salary": 89780,
        "Senior Management": "true",
        "Start Date": "Thu, 23 Jun 2005 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "9.601",
        "First Name": "Irene",
        "Gender": "Female",
        "Last Login Time": "2:14 PM",
        "Salary": 125018,
        "Senior Management": "true",
        "Start Date": "Wed, 29 Nov 2006 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "18.769",
        "First Name": "Janet",
        "Gender": "Female",
        "Last Login Time": "12:10 PM",
        "Salary": 36927,
        "Senior Management": "false",
        "Start Date": "Sat, 12 Jul 2008 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "14.227",
        "First Name": "Joyce",
        "Gender": "Female",
        "Last Login Time": "7:38 AM",
        "Salary": 50701,
        "Senior Management": "true",
        "Start Date": "Tue, 07 Feb 1995 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "16.807",
        "First Name": "Joyce",
        "Gender": "Female",
        "Last Login Time": "6:04 AM",
        "Salary": 51065,
        "Senior Management": "false",
        "Start Date": "Wed, 25 Jul 2001 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "2.664",
        "First Name": "Julia",
        "Gender": "Female",
        "Last Login Time": "12:52 PM",
        "Salary": 36403,
        "Senior Management": "true",
        "Start Date": "Tue, 02 Mar 1982 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "2.147",
        "First Name": "Julia",
        "Gender": "Female",
        "Last Login Time": "3:12 AM",
        "Salary": 97566,
        "Senior Management": "false",
        "Start Date": "Mon, 18 Aug 2014 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "12.637",
        "First Name": "Julie",
        "Gender": "Female",
        "Last Login Time": "3:19 PM",
        "Salary": 102508,
        "Senior Management": "true",
        "Start Date": "Sun, 26 Oct 1997 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "3.55",
        "First Name": "Julie",
        "Gender": "Female",
        "Last Login Time": "1:52 PM",
        "Salary": 109588,
        "Senior Management": "false",
        "Start Date": "Sun, 23 Jul 1989 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "7.507",
        "First Name": "Julie",
        "Gender": "Female",
        "Last Login Time": "9:26 AM",
        "Salary": 56926,
        "Senior Management": "false",
        "Start Date": "Sun, 23 Mar 1986 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "2.518",
        "First Name": "Julie",
        "Gender": "Female",
        "Last Login Time": "5:52 AM",
        "Salary": 73437,
        "Senior Management": "true",
        "Start Date": "Thu, 23 Apr 1998 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "3.459",
        "First Name": "Julie",
        "Gender": "Female",
        "Last Login Time": "5:13 AM",
        "Salary": 145357,
        "Senior Management": "false",
        "Start Date": "Sat, 08 Mar 1980 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "17.653",
        "First Name": "Karen",
        "Gender": "Female",
        "Last Login Time": "7:46 AM",
        "Salary": 102488,
        "Senior Management": "true",
        "Start Date": "Tue, 30 Nov 1999 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "16.552",
        "First Name": "Karen",
        "Gender": "Female",
        "Last Login Time": "10:09 PM",
        "Salary": 46478,
        "Senior Management": "false",
        "Start Date": "Thu, 09 Jan 2014 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "16.306",
        "First Name": "Karen",
        "Gender": "Female",
        "Last Login Time": "4:56 PM",
        "Salary": 80633,
        "Senior Management": "false",
        "Start Date": "Fri, 29 Aug 1997 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "9",
        "First Name": "Kathy",
        "Gender": "Female",
        "Last Login Time": "4:51 AM",
        "Salary": 66820,
        "Senior Management": "true",
        "Start Date": "Wed, 22 Jun 2005 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "8.567",
        "First Name": "Kathy",
        "Gender": "Female",
        "Last Login Time": "4:33 AM",
        "Salary": 91712,
        "Senior Management": "false",
        "Start Date": "Sat, 09 Mar 1996 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "16.991",
        "First Name": "Kathy",
        "Gender": "Female",
        "Last Login Time": "7:26 PM",
        "Salary": 149563,
        "Senior Management": "true",
        "Start Date": "Sat, 18 Mar 2000 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "9.404",
        "First Name": "Kathy",
        "Gender": "Female",
        "Last Login Time": "12:46 AM",
        "Salary": 50905,
        "Senior Management": "true",
        "Start Date": "Wed, 19 Apr 1995 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "8.34",
        "First Name": "Kathy",
        "Gender": "Female",
        "Last Login Time": "3:09 PM",
        "Salary": 132381,
        "Senior Management": "false",
        "Start Date": "Wed, 18 Dec 2013 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "7.094",
        "First Name": "Kathy",
        "Gender": "Female",
        "Last Login Time": "9:55 PM",
        "Salary": 93753,
        "Senior Management": "true",
        "Start Date": "Sun, 25 Nov 2001 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "18.492",
        "First Name": "Kathy",
        "Gender": "Female",
        "Last Login Time": "6:19 PM",
        "Salary": 86318,
        "Senior Management": "true",
        "Start Date": "Fri, 08 May 1987 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "8.461",
        "First Name": "Kathy",
        "Gender": "Female",
        "Last Login Time": "12:59 PM",
        "Salary": 143541,
        "Senior Management": "false",
        "Start Date": "Fri, 25 Oct 1996 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "1.451",
        "First Name": "Kathy",
        "Gender": "Female",
        "Last Login Time": "5:11 AM",
        "Salary": 45682,
        "Senior Management": "true",
        "Start Date": "Sun, 14 Jan 2001 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "1.431",
        "First Name": "Kelly",
        "Gender": "Female",
        "Last Login Time": "3:09 AM",
        "Salary": 41427,
        "Senior Management": "false",
        "Start Date": "Fri, 16 Aug 1996 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "4.068",
        "First Name": "Kelly",
        "Gender": "Female",
        "Last Login Time": "6:20 PM",
        "Salary": 39371,
        "Senior Management": "false",
        "Start Date": "Sat, 17 Mar 2007 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "2.624",
        "First Name": "Laura",
        "Gender": "Female",
        "Last Login Time": "1:57 PM",
        "Salary": 42087,
        "Senior Management": "false",
        "Start Date": "Sun, 02 Apr 2006 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "3.96",
        "First Name": "Laura",
        "Gender": "Female",
        "Last Login Time": "6:07 PM",
        "Salary": 84672,
        "Senior Management": "false",
        "Start Date": "Wed, 12 Jul 2000 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "9.557",
        "First Name": "Linda",
        "Gender": "Female",
        "Last Login Time": "8:49 PM",
        "Salary": 57427,
        "Senior Management": "true",
        "Start Date": "Mon, 19 Oct 1981 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "12.506",
        "First Name": "Linda",
        "Gender": "Female",
        "Last Login Time": "5:45 PM",
        "Salary": 119009,
        "Senior Management": "true",
        "Start Date": "Thu, 25 May 2000 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "19.612",
        "First Name": "Linda",
        "Gender": "Female",
        "Last Login Time": "12:04 PM",
        "Salary": 110967,
        "Senior Management": "true",
        "Start Date": "Sat, 24 Jun 2006 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "3.041",
        "First Name": "Linda",
        "Gender": "Female",
        "Last Login Time": "2:20 AM",
        "Salary": 115658,
        "Senior Management": "true",
        "Start Date": "Sun, 16 Dec 1990 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "2.194",
        "First Name": "Linda",
        "Gender": "Female",
        "Last Login Time": "10:12 PM",
        "Salary": 144001,
        "Senior Management": "false",
        "Start Date": "Wed, 15 Jul 2009 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "13.295",
        "First Name": "Linda",
        "Gender": "Female",
        "Last Login Time": "4:34 AM",
        "Salary": 51431,
        "Senior Management": "false",
        "Start Date": "Sun, 18 Aug 1985 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "17.308",
        "First Name": "Linda",
        "Gender": "Female",
        "Last Login Time": "8:49 PM",
        "Salary": 44486,
        "Senior Management": "true",
        "Start Date": "Thu, 04 Feb 2010 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "11.858",
        "First Name": "Maria",
        "Gender": "Female",
        "Last Login Time": "11:17 AM",
        "Salary": 130590,
        "Senior Management": "false",
        "Start Date": "Fri, 23 Apr 1993 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "9.64",
        "First Name": "Maria",
        "Gender": "Female",
        "Last Login Time": "9:57 PM",
        "Salary": 36067,
        "Senior Management": "true",
        "Start Date": "Thu, 27 Dec 1990 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "10.056",
        "First Name": "Maria",
        "Gender": "Female",
        "Last Login Time": "5:23 PM",
        "Salary": 96250,
        "Senior Management": "false",
        "Start Date": "Fri, 14 Mar 2003 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "13.04",
        "First Name": "Maria",
        "Gender": "Female",
        "Last Login Time": "4:53 PM",
        "Salary": 43455,
        "Senior Management": "false",
        "Start Date": "Sat, 15 Oct 2011 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "17.695",
        "First Name": "Marie",
        "Gender": "Female",
        "Last Login Time": "12:12 AM",
        "Salary": 104058,
        "Senior Management": "true",
        "Start Date": "Sun, 16 Mar 2003 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "13.677",
        "First Name": "Marie",
        "Gender": "Female",
        "Last Login Time": "1:58 PM",
        "Salary": 100308,
        "Senior Management": "false",
        "Start Date": "Sun, 06 Aug 1995 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "10.966",
        "First Name": "Marie",
        "Gender": "Female",
        "Last Login Time": "8:05 PM",
        "Salary": 123711,
        "Senior Management": "false",
        "Start Date": "Thu, 03 Oct 2013 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "10.247",
        "First Name": "Marie",
        "Gender": "Female",
        "Last Login Time": "10:09 PM",
        "Salary": 62666,
        "Senior Management": "false",
        "Start Date": "Thu, 20 Oct 2011 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "4.644",
        "First Name": "Marie",
        "Gender": "Female",
        "Last Login Time": "5:06 AM",
        "Salary": 125574,
        "Senior Management": "false",
        "Start Date": "Thu, 23 Nov 2000 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "18.685",
        "First Name": "Marie",
        "Gender": "Female",
        "Last Login Time": "2:01 PM",
        "Salary": 145988,
        "Senior Management": "true",
        "Start Date": "Fri, 08 Apr 1983 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "7.943",
        "First Name": "Marie",
        "Gender": "Female",
        "Last Login Time": "6:28 PM",
        "Salary": 98406,
        "Senior Management": "true",
        "Start Date": "Wed, 08 Dec 1993 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "13.83",
        "First Name": "Nancy",
        "Gender": "Female",
        "Last Login Time": "8:05 AM",
        "Salary": 94976,
        "Senior Management": "true",
        "Start Date": "Sat, 23 Sep 2000 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "2.672",
        "First Name": "Nancy",
        "Gender": "Female",
        "Last Login Time": "11:57 PM",
        "Salary": 125250,
        "Senior Management": "true",
        "Start Date": "Sat, 15 Dec 2012 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "3.512",
        "First Name": "Nancy",
        "Gender": "Female",
        "Last Login Time": "10:20 PM",
        "Salary": 121006,
        "Senior Management": "true",
        "Start Date": "Tue, 07 May 1985 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "2.386",
        "First Name": "Nancy",
        "Gender": "Female",
        "Last Login Time": "11:57 PM",
        "Salary": 85213,
        "Senior Management": "true",
        "Start Date": "Mon, 10 Sep 2001 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "8.756",
        "First Name": "Norma",
        "Gender": "Female",
        "Last Login Time": "8:45 PM",
        "Salary": 114412,
        "Senior Management": "true",
        "Start Date": "Sun, 28 Feb 1999 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "3.643",
        "First Name": "Norma",
        "Gender": "Female",
        "Last Login Time": "11:44 PM",
        "Salary": 94393,
        "Senior Management": "true",
        "Start Date": "Wed, 11 Feb 2015 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "9.302",
        "First Name": "Norma",
        "Gender": "Female",
        "Last Login Time": "5:40 AM",
        "Salary": 38872,
        "Senior Management": "true",
        "Start Date": "Tue, 16 Apr 1996 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "10.833",
        "First Name": "Paula",
        "Gender": "Female",
        "Last Login Time": "11:42 AM",
        "Salary": 58423,
        "Senior Management": "false",
        "Start Date": "Sat, 21 May 1983 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "5.965",
        "First Name": "Robin",
        "Gender": "Female",
        "Last Login Time": "3:15 PM",
        "Salary": 114797,
        "Senior Management": "true",
        "Start Date": "Sat, 04 Jun 1983 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "5.025",
        "First Name": "Robin",
        "Gender": "Female",
        "Last Login Time": "2:12 AM",
        "Salary": 111163,
        "Senior Management": "true",
        "Start Date": "Thu, 08 Jan 1998 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "9.66",
        "First Name": "Robin",
        "Gender": "Female",
        "Last Login Time": "5:41 PM",
        "Salary": 70248,
        "Senior Management": "true",
        "Start Date": "Fri, 26 Mar 2004 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "19.239",
        "First Name": "Robin",
        "Gender": "Female",
        "Last Login Time": "2:44 AM",
        "Salary": 41808,
        "Senior Management": "false",
        "Start Date": "Mon, 01 Oct 2012 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "10.982",
        "First Name": "Robin",
        "Gender": "Female",
        "Last Login Time": "1:35 PM",
        "Salary": 100765,
        "Senior Management": "true",
        "Start Date": "Fri, 24 Jul 1987 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "2.311",
        "First Name": "Sarah",
        "Gender": "Female",
        "Last Login Time": "7:50 AM",
        "Salary": 87298,
        "Senior Management": "false",
        "Start Date": "Thu, 14 Sep 1995 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "7.824",
        "First Name": "Sarah",
        "Gender": "Female",
        "Last Login Time": "7:06 AM",
        "Salary": 64207,
        "Senior Management": "true",
        "Start Date": "Sun, 22 May 1994 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "1.763",
        "First Name": "Sarah",
        "Gender": "Female",
        "Last Login Time": "2:47 PM",
        "Salary": 37259,
        "Senior Management": "false",
        "Start Date": "Mon, 03 Nov 1980 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "5.146",
        "First Name": "Sarah",
        "Gender": "Female",
        "Last Login Time": "11:17 AM",
        "Salary": 109517,
        "Senior Management": "false",
        "Start Date": "Tue, 06 Apr 1999 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "11.176",
        "First Name": "Sarah",
        "Gender": "Female",
        "Last Login Time": "11:08 PM",
        "Salary": 127118,
        "Senior Management": "false",
        "Start Date": "Sun, 17 Aug 2014 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "5.949",
        "First Name": "Sarah",
        "Gender": "Female",
        "Last Login Time": "9:16 AM",
        "Salary": 124566,
        "Senior Management": "false",
        "Start Date": "Mon, 04 Dec 1995 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "18.892",
        "First Name": "Susan",
        "Gender": "Female",
        "Last Login Time": "1:30 AM",
        "Salary": 80688,
        "Senior Management": "true",
        "Start Date": "Sat, 25 Sep 2004 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "19.142",
        "First Name": "Susan",
        "Gender": "Female",
        "Last Login Time": "9:31 AM",
        "Salary": 90829,
        "Senior Management": "false",
        "Start Date": "Fri, 18 Apr 1986 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "12.467",
        "First Name": "Susan",
        "Gender": "Female",
        "Last Login Time": "10:05 PM",
        "Salary": 92436,
        "Senior Management": "false",
        "Start Date": "Fri, 07 Apr 1995 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "17.463",
        "First Name": "Tammy",
        "Gender": "Female",
        "Last Login Time": "10:30 AM",
        "Salary": 132839,
        "Senior Management": "true",
        "Start Date": "Sun, 11 Nov 1984 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "7.132",
        "First Name": "Wanda",
        "Gender": "Female",
        "Last Login Time": "1:44 PM",
        "Salary": 65362,
        "Senior Management": "true",
        "Start Date": "Sun, 20 Jul 2008 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "19.695",
        "First Name": "Wanda",
        "Gender": "Female",
        "Last Login Time": "3:11 AM",
        "Salary": 78883,
        "Senior Management": "false",
        "Start Date": "Tue, 06 Apr 1993 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "14.077",
        "First Name": "Amanda",
        "Gender": "Female",
        "Last Login Time": "1:32 PM",
        "Salary": 80803,
        "Senior Management": "true",
        "Start Date": "Sun, 01 Aug 2004 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "13.853",
        "First Name": "Amanda",
        "Gender": "Female",
        "Last Login Time": "7:46 AM",
        "Salary": 109290,
        "Senior Management": "false",
        "Start Date": "Fri, 07 Jun 2002 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "1.438",
        "First Name": "Amanda",
        "Gender": "Female",
        "Last Login Time": "11:46 PM",
        "Salary": 107111,
        "Senior Management": "true",
        "Start Date": "Wed, 17 Mar 1982 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "5.203",
        "First Name": "Amanda",
        "Gender": "Female",
        "Last Login Time": "5:06 AM",
        "Salary": 102081,
        "Senior Management": "false",
        "Start Date": "Wed, 25 Jan 1995 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "9.557",
        "First Name": "Andrea",
        "Gender": "Female",
        "Last Login Time": "5:43 AM",
        "Salary": 120204,
        "Senior Management": "false",
        "Start Date": "Thu, 12 Jan 2012 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "12.121",
        "First Name": "Andrea",
        "Gender": "Female",
        "Last Login Time": "10:30 PM",
        "Salary": 115913,
        "Senior Management": "false",
        "Start Date": "Sun, 14 Sep 2003 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "19.422",
        "First Name": "Andrea",
        "Gender": "Female",
        "Last Login Time": "11:54 AM",
        "Salary": 79123,
        "Senior Management": "false",
        "Start Date": "Fri, 01 Oct 2010 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "13.346",
        "First Name": "Andrea",
        "Gender": "Female",
        "Last Login Time": "11:23 AM",
        "Salary": 87575,
        "Senior Management": "true",
        "Start Date": "Sun, 30 Oct 1994 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "6.5",
        "First Name": "Andrea",
        "Gender": "Female",
        "Last Login Time": "2:37 PM",
        "Salary": 123591,
        "Senior Management": "true",
        "Start Date": "Thu, 17 Nov 2011 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "12.866",
        "First Name": "Andrea",
        "Gender": "Female",
        "Last Login Time": "11:10 PM",
        "Salary": 113760,
        "Senior Management": "true",
        "Start Date": "Thu, 31 Aug 1989 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "13.47",
        "First Name": "Andrea",
        "Gender": "Female",
        "Last Login Time": "6:40 AM",
        "Salary": 37888,
        "Senior Management": "false",
        "Start Date": "Mon, 10 Dec 2001 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "13.707",
        "First Name": "Andrea",
        "Gender": "Female",
        "Last Login Time": "9:25 AM",
        "Salary": 149105,
        "Senior Management": "true",
        "Start Date": "Thu, 22 Jul 1999 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "18.523",
        "First Name": "Angela",
        "Gender": "Female",
        "Last Login Time": "6:29 AM",
        "Salary": 95570,
        "Senior Management": "true",
        "Start Date": "Tue, 22 Nov 2005 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "6.811",
        "First Name": "Ashley",
        "Gender": "Female",
        "Last Login Time": "11:00 AM",
        "Salary": 58698,
        "Senior Management": "true",
        "Start Date": "Sun, 04 Aug 2002 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "6.03",
        "First Name": "Ashley",
        "Gender": "Female",
        "Last Login Time": "11:30 AM",
        "Salary": 112238,
        "Senior Management": "true",
        "Start Date": "Thu, 25 May 2006 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "1.985",
        "First Name": "Ashley",
        "Gender": "Female",
        "Last Login Time": "9:48 PM",
        "Salary": 142415,
        "Senior Management": "true",
        "Start Date": "Fri, 15 Aug 1997 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "6.51",
        "First Name": "Ashley",
        "Gender": "Female",
        "Last Login Time": "9:18 PM",
        "Salary": 120675,
        "Senior Management": "false",
        "Start Date": "Wed, 17 Nov 1999 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "11.048",
        "First Name": "Ashley",
        "Gender": "Female",
        "Last Login Time": "1:24 PM",
        "Salary": 142410,
        "Senior Management": "true",
        "Start Date": "Fri, 31 Mar 2006 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "5.118",
        "First Name": "Bonnie",
        "Gender": "Female",
        "Last Login Time": "1:27 AM",
        "Salary": 104897,
        "Senior Management": "true",
        "Start Date": "Tue, 02 Jul 1991 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "4.99",
        "First Name": "Bonnie",
        "Gender": "Female",
        "Last Login Time": "3:30 PM",
        "Salary": 115814,
        "Senior Management": "false",
        "Start Date": "Sun, 13 Nov 1988 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "8.454",
        "First Name": "Bonnie",
        "Gender": "Female",
        "Last Login Time": "3:12 PM",
        "Salary": 42153,
        "Senior Management": "true",
        "Start Date": "Fri, 17 Dec 1999 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "14.249",
        "First Name": "Bonnie",
        "Gender": "Female",
        "Last Login Time": "2:17 AM",
        "Salary": 131943,
        "Senior Management": "false",
        "Start Date": "Wed, 25 Aug 2004 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "2.01",
        "First Name": "Bonnie",
        "Gender": "Female",
        "Last Login Time": "9:26 AM",
        "Salary": 90427,
        "Senior Management": "true",
        "Start Date": "Tue, 23 Dec 2008 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "4.337",
        "First Name": "Brenda",
        "Gender": "Female",
        "Last Login Time": "9:33 PM",
        "Salary": 141521,
        "Senior Management": "false",
        "Start Date": "Thu, 06 Oct 2005 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "2.675",
        "First Name": "Brenda",
        "Gender": "Female",
        "Last Login Time": "7:12 AM",
        "Salary": 87715,
        "Senior Management": "false",
        "Start Date": "Tue, 17 Apr 1984 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "11.682",
        "First Name": "Brenda",
        "Gender": "Female",
        "Last Login Time": "6:01 PM",
        "Salary": 131131,
        "Senior Management": "false",
        "Start Date": "Sat, 03 Jan 1981 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "19.332",
        "First Name": "Brenda",
        "Gender": "Female",
        "Last Login Time": "4:39 PM",
        "Salary": 73749,
        "Senior Management": "false",
        "Start Date": "Sun, 18 Jan 2015 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "9.375",
        "First Name": "Cheryl",
        "Gender": "Female",
        "Last Login Time": "2:57 AM",
        "Salary": 52080,
        "Senior Management": "false",
        "Start Date": "Tue, 23 Sep 2008 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "2.196",
        "First Name": "Cheryl",
        "Gender": "Female",
        "Last Login Time": "10:16 AM",
        "Salary": 81308,
        "Senior Management": "true",
        "Start Date": "Tue, 08 Sep 2009 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "15.85",
        "First Name": "Cheryl",
        "Gender": "Female",
        "Last Login Time": "8:33 AM",
        "Salary": 67150,
        "Senior Management": "true",
        "Start Date": "Tue, 16 Aug 1994 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "15.918",
        "First Name": "Cheryl",
        "Gender": "Female",
        "Last Login Time": "9:27 AM",
        "Salary": 71751,
        "Senior Management": "false",
        "Start Date": "Wed, 03 Dec 2014 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "8.945",
        "First Name": "Cheryl",
        "Gender": "Female",
        "Last Login Time": "6:28 AM",
        "Salary": 98841,
        "Senior Management": "true",
        "Start Date": "Fri, 23 Jul 1982 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "3.699",
        "First Name": "Denise",
        "Gender": "Female",
        "Last Login Time": "12:03 PM",
        "Salary": 106862,
        "Senior Management": "false",
        "Start Date": "Tue, 06 Nov 2001 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "5.108",
        "First Name": "Denise",
        "Gender": "Female",
        "Last Login Time": "7:57 AM",
        "Salary": 115118,
        "Senior Management": "false",
        "Start Date": "Fri, 20 Mar 2009 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "11.196",
        "First Name": "Denise",
        "Gender": "Female",
        "Last Login Time": "12:02 AM",
        "Salary": 36697,
        "Senior Management": "true",
        "Start Date": "Sun, 18 Mar 2001 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "3.997",
        "First Name": "Denise",
        "Gender": "Female",
        "Last Login Time": "6:22 AM",
        "Salary": 86150,
        "Senior Management": "false",
        "Start Date": "Sun, 19 Feb 1984 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "4.195",
        "First Name": "Denise",
        "Gender": "Female",
        "Last Login Time": "5:42 AM",
        "Salary": 137954,
        "Senior Management": "true",
        "Start Date": "Mon, 19 Oct 1992 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "15.364",
        "First Name": "Evelyn",
        "Gender": "Female",
        "Last Login Time": "11:10 PM",
        "Salary": 81673,
        "Senior Management": "true",
        "Start Date": "Sat, 24 May 1980 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "17.269",
        "First Name": "Evelyn",
        "Gender": "Female",
        "Last Login Time": "1:58 PM",
        "Salary": 36759,
        "Senior Management": "true",
        "Start Date": "Sat, 03 Sep 1983 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "10.366",
        "First Name": "Evelyn",
        "Gender": "Female",
        "Last Login Time": "7:55 PM",
        "Salary": 51525,
        "Senior Management": "false",
        "Start Date": "Tue, 22 Sep 1998 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "19.767",
        "First Name": "Evelyn",
        "Gender": "Female",
        "Last Login Time": "4:44 AM",
        "Salary": 123621,
        "Senior Management": "true",
        "Start Date": "Sun, 10 Feb 2002 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "8.833",
        "First Name": "Gloria",
        "Gender": "Female",
        "Last Login Time": "5:34 AM",
        "Salary": 134148,
        "Senior Management": "true",
        "Start Date": "Fri, 29 Jun 2007 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "2.491",
        "First Name": "Gloria",
        "Gender": "Female",
        "Last Login Time": "1:44 AM",
        "Salary": 90730,
        "Senior Management": "false",
        "Start Date": "Tue, 27 Mar 2007 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "11.312",
        "First Name": "Gloria",
        "Gender": "Female",
        "Last Login Time": "7:40 PM",
        "Salary": 131045,
        "Senior Management": "true",
        "Start Date": "Tue, 19 Sep 1989 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "15.979",
        "First Name": "Gloria",
        "Gender": "Female",
        "Last Login Time": "8:26 PM",
        "Salary": 66224,
        "Senior Management": "true",
        "Start Date": "Sun, 12 Apr 1992 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "1.027",
        "First Name": "Gloria",
        "Gender": "Female",
        "Last Login Time": "10:31 AM",
        "Salary": 46602,
        "Senior Management": "true",
        "Start Date": "Thu, 19 Aug 2004 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "9.631",
        "First Name": "Gloria",
        "Gender": "Female",
        "Last Login Time": "4:43 AM",
        "Salary": 39833,
        "Senior Management": "false",
        "Start Date": "Sat, 24 Oct 1987 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "10.331",
        "First Name": "Gloria",
        "Gender": "Female",
        "Last Login Time": "5:08 AM",
        "Salary": 136709,
        "Senior Management": "true",
        "Start Date": "Mon, 08 Dec 2014 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "11.955",
        "First Name": "Janice",
        "Gender": "Female",
        "Last Login Time": "12:40 AM",
        "Salary": 51082,
        "Senior Management": "false",
        "Start Date": "Sat, 12 Mar 2016 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "10.696",
        "First Name": "Janice",
        "Gender": "Female",
        "Last Login Time": "1:48 PM",
        "Salary": 136032,
        "Senior Management": "true",
        "Start Date": "Sat, 28 Jun 1997 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "3.311",
        "First Name": "Janice",
        "Gender": "Female",
        "Last Login Time": "9:06 PM",
        "Salary": 41190,
        "Senior Management": "true",
        "Start Date": "Mon, 02 Jan 1984 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "3.283",
        "First Name": "Janice",
        "Gender": "Female",
        "Last Login Time": "6:42 AM",
        "Salary": 102697,
        "Senior Management": "false",
        "Start Date": "Thu, 17 Dec 2009 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "7.461",
        "First Name": "Judith",
        "Gender": "Female",
        "Last Login Time": "1:22 PM",
        "Salary": 117055,
        "Senior Management": "false",
        "Start Date": "Fri, 23 Nov 2007 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "6.818",
        "First Name": "Judith",
        "Gender": "Female",
        "Last Login Time": "11:16 AM",
        "Salary": 134048,
        "Senior Management": "true",
        "Start Date": "Sun, 03 Sep 1989 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "19.488",
        "First Name": "Judith",
        "Gender": "Female",
        "Last Login Time": "7:32 AM",
        "Salary": 109324,
        "Senior Management": "false",
        "Start Date": "Mon, 01 Mar 2004 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "15.132",
        "First Name": "Louise",
        "Gender": "Female",
        "Last Login Time": "9:01 AM",
        "Salary": 63241,
        "Senior Management": "true",
        "Start Date": "Tue, 12 Aug 1980 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "1.886",
        "First Name": "Louise",
        "Gender": "Female",
        "Last Login Time": "9:47 AM",
        "Salary": 46666,
        "Senior Management": "true",
        "Start Date": "Tue, 13 May 2003 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "8.205",
        "First Name": "Louise",
        "Gender": "Female",
        "Last Login Time": "5:47 AM",
        "Salary": 91462,
        "Senior Management": "false",
        "Start Date": "Fri, 18 Sep 1981 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "8.965",
        "First Name": "Louise",
        "Gender": "Female",
        "Last Login Time": "1:03 AM",
        "Salary": 106362,
        "Senior Management": "false",
        "Start Date": "Fri, 26 Feb 1982 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "11.671",
        "First Name": "Louise",
        "Gender": "Female",
        "Last Login Time": "10:27 PM",
        "Salary": 43050,
        "Senior Management": "false",
        "Start Date": "Mon, 27 Mar 1995 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "14.782",
        "First Name": "Martha",
        "Gender": "Female",
        "Last Login Time": "3:22 AM",
        "Salary": 135758,
        "Senior Management": "true",
        "Start Date": "Fri, 14 Sep 2001 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "19.626",
        "First Name": "Martha",
        "Gender": "Female",
        "Last Login Time": "11:11 PM",
        "Salary": 94963,
        "Senior Management": "true",
        "Start Date": "Thu, 17 Jul 1997 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "18.674",
        "First Name": "Nicole",
        "Gender": "Female",
        "Last Login Time": "12:40 AM",
        "Salary": 66047,
        "Senior Management": "true",
        "Start Date": "Sun, 26 Apr 2009 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "10.286",
        "First Name": "Nicole",
        "Gender": "Female",
        "Last Login Time": "5:17 PM",
        "Salary": 44021,
        "Senior Management": "false",
        "Start Date": "Mon, 01 Mar 2004 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "4.166",
        "First Name": "Pamela",
        "Gender": "Female",
        "Last Login Time": "6:51 AM",
        "Salary": 54585,
        "Senior Management": "false",
        "Start Date": "Thu, 01 Jul 1982 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "12.599",
        "First Name": "Rachel",
        "Gender": "Female",
        "Last Login Time": "8:47 PM",
        "Salary": 142032,
        "Senior Management": "false",
        "Start Date": "Mon, 16 Feb 2009 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "9.735",
        "First Name": "Rachel",
        "Gender": "Female",
        "Last Login Time": "6:53 AM",
        "Salary": 51178,
        "Senior Management": "true",
        "Start Date": "Mon, 16 Aug 1999 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "7.808",
        "First Name": "Rachel",
        "Gender": "Female",
        "Last Login Time": "12:01 PM",
        "Salary": 110924,
        "Senior Management": "false",
        "Start Date": "Fri, 22 Apr 1988 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "3.221",
        "First Name": "Rachel",
        "Gender": "Female",
        "Last Login Time": "12:52 AM",
        "Salary": 54941,
        "Senior Management": "true",
        "Start Date": "Thu, 23 Jun 2011 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "8.842",
        "First Name": "Sandra",
        "Gender": "Female",
        "Last Login Time": "7:25 AM",
        "Salary": 42090,
        "Senior Management": "true",
        "Start Date": "Wed, 19 Jan 1983 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "9.657",
        "First Name": "Sandra",
        "Gender": "Female",
        "Last Login Time": "7:14 PM",
        "Salary": 116931,
        "Senior Management": "true",
        "Start Date": "Mon, 24 Apr 1995 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "2.58",
        "First Name": "Sandra",
        "Gender": "Female",
        "Last Login Time": "4:17 PM",
        "Salary": 111468,
        "Senior Management": "true",
        "Start Date": "Thu, 07 Sep 1989 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "19.264",
        "First Name": "Sandra",
        "Gender": "Female",
        "Last Login Time": "12:39 PM",
        "Salary": 132327,
        "Senior Management": "false",
        "Start Date": "Sat, 07 Feb 1998 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "7.564",
        "First Name": "Sharon",
        "Gender": "Female",
        "Last Login Time": "4:39 PM",
        "Salary": 91522,
        "Senior Management": "false",
        "Start Date": "Sun, 09 Mar 2014 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "14.693",
        "First Name": "Sharon",
        "Gender": "Female",
        "Last Login Time": "6:32 AM",
        "Salary": 147635,
        "Senior Management": "false",
        "Start Date": "Tue, 12 Mar 2002 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "19.731",
        "First Name": "Sharon",
        "Gender": "Female",
        "Last Login Time": "9:50 AM",
        "Salary": 46007,
        "Senior Management": "true",
        "Start Date": "Fri, 01 Jul 2011 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "8.294",
        "First Name": "Teresa",
        "Gender": "Female",
        "Last Login Time": "7:37 PM",
        "Salary": 69740,
        "Senior Management": "false",
        "Start Date": "Wed, 24 Jun 1987 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "11.907",
        "First Name": "Teresa",
        "Gender": "Female",
        "Last Login Time": "3:17 PM",
        "Salary": 113425,
        "Senior Management": "true",
        "Start Date": "Tue, 22 Jan 2013 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "7.25",
        "First Name": "Barbara",
        "Gender": "Female",
        "Last Login Time": "8:02 AM",
        "Salary": 47322,
        "Senior Management": "true",
        "Start Date": "Thu, 21 Mar 2002 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "8.696",
        "First Name": "Barbara",
        "Gender": "Female",
        "Last Login Time": "8:11 AM",
        "Salary": 144677,
        "Senior Management": "false",
        "Start Date": "Mon, 22 Mar 2004 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "11.905",
        "First Name": "Barbara",
        "Gender": "Female",
        "Last Login Time": "3:41 PM",
        "Salary": 127297,
        "Senior Management": "true",
        "Start Date": "Mon, 02 Sep 1991 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "13.326",
        "First Name": "Barbara",
        "Gender": "Female",
        "Last Login Time": "12:35 AM",
        "Salary": 85718,
        "Senior Management": "false",
        "Start Date": "Sat, 12 Nov 2011 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "6.837",
        "First Name": "Barbara",
        "Gender": "Female",
        "Last Login Time": "5:32 AM",
        "Salary": 82884,
        "Senior Management": "true",
        "Start Date": "Tue, 26 Nov 2002 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "15.835",
        "First Name": "Beverly",
        "Gender": "Female",
        "Last Login Time": "8:26 PM",
        "Salary": 121918,
        "Senior Management": "false",
        "Start Date": "Wed, 09 Sep 1998 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "3.665",
        "First Name": "Beverly",
        "Gender": "Female",
        "Last Login Time": "2:57 AM",
        "Salary": 107163,
        "Senior Management": "true",
        "Start Date": "Wed, 30 Nov 2005 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "19.064",
        "First Name": "Beverly",
        "Gender": "Female",
        "Last Login Time": "2:45 PM",
        "Salary": 59070,
        "Senior Management": "true",
        "Start Date": "Mon, 22 Oct 1990 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "9.212",
        "First Name": "Beverly",
        "Gender": "Female",
        "Last Login Time": "2:27 PM",
        "Salary": 76485,
        "Senior Management": "true",
        "Start Date": "Sat, 11 Apr 1998 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "8.115",
        "First Name": "Beverly",
        "Gender": "Female",
        "Last Login Time": "12:51 AM",
        "Salary": 80838,
        "Senior Management": "false",
        "Start Date": "Fri, 17 Oct 1986 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "2.65",
        "First Name": "Carolyn",
        "Gender": "Female",
        "Last Login Time": "5:38 AM",
        "Salary": 109260,
        "Senior Management": "true",
        "Start Date": "Sat, 09 Apr 2011 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "3.031",
        "First Name": "Carolyn",
        "Gender": "Female",
        "Last Login Time": "3:51 AM",
        "Salary": 69268,
        "Senior Management": "false",
        "Start Date": "Tue, 06 Nov 2012 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "13.492",
        "First Name": "Carolyn",
        "Gender": "Female",
        "Last Login Time": "6:38 AM",
        "Salary": 118037,
        "Senior Management": "false",
        "Start Date": "Wed, 17 Mar 2004 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "7.482",
        "First Name": "Cynthia",
        "Gender": "Female",
        "Last Login Time": "6:54 PM",
        "Salary": 145146,
        "Senior Management": "true",
        "Start Date": "Wed, 16 Nov 1988 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "1.737",
        "First Name": "Cynthia",
        "Gender": "Female",
        "Last Login Time": "8:34 AM",
        "Salary": 142321,
        "Senior Management": "false",
        "Start Date": "Mon, 21 Mar 1994 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "10.751",
        "First Name": "Cynthia",
        "Gender": "Female",
        "Last Login Time": "11:03 PM",
        "Salary": 74287,
        "Senior Management": "false",
        "Start Date": "Mon, 03 Dec 2012 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "13.472",
        "First Name": "Cynthia",
        "Gender": "Female",
        "Last Login Time": "1:08 PM",
        "Salary": 51633,
        "Senior Management": "true",
        "Start Date": "Sat, 14 Sep 1991 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "2.419",
        "First Name": "Cynthia",
        "Gender": "Female",
        "Last Login Time": "3:19 AM",
        "Salary": 78226,
        "Senior Management": "false",
        "Start Date": "Fri, 23 May 1980 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "8.701",
        "First Name": "Cynthia",
        "Gender": "Female",
        "Last Login Time": "6:38 AM",
        "Salary": 82408,
        "Senior Management": "true",
        "Start Date": "Mon, 29 Jun 2015 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "11.749",
        "First Name": "Cynthia",
        "Gender": "Female",
        "Last Login Time": "1:24 AM",
        "Salary": 35381,
        "Senior Management": "false",
        "Start Date": "Sat, 05 Jul 1986 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "7.864",
        "First Name": "Cynthia",
        "Gender": "Female",
        "Last Login Time": "8:55 AM",
        "Salary": 149684,
        "Senior Management": "false",
        "Start Date": "Wed, 12 Jul 2006 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "17.436",
        "First Name": "Deborah",
        "Gender": "Female",
        "Last Login Time": "4:33 AM",
        "Salary": 46953,
        "Senior Management": "false",
        "Start Date": "Tue, 25 Nov 1980 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "17.371",
        "First Name": "Deborah",
        "Gender": "Female",
        "Last Login Time": "1:40 PM",
        "Salary": 113129,
        "Senior Management": "false",
        "Start Date": "Thu, 21 Nov 1985 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "5.268",
        "First Name": "Deborah",
        "Gender": "Female",
        "Last Login Time": "6:55 PM",
        "Salary": 105573,
        "Senior Management": "true",
        "Start Date": "Sun, 23 Apr 2000 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "7.266",
        "First Name": "Deborah",
        "Gender": "Female",
        "Last Login Time": "10:17 AM",
        "Salary": 118043,
        "Senior Management": "true",
        "Start Date": "Thu, 26 Feb 2009 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "9.624",
        "First Name": "Deborah",
        "Gender": "Female",
        "Last Login Time": "4:53 PM",
        "Salary": 60003,
        "Senior Management": "false",
        "Start Date": "Tue, 11 Nov 2003 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "3.12",
        "First Name": "Dorothy",
        "Gender": "Female",
        "Last Login Time": "10:50 PM",
        "Salary": 140136,
        "Senior Management": "true",
        "Start Date": "Tue, 05 Nov 2013 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "19.111",
        "First Name": "Dorothy",
        "Gender": "Female",
        "Last Login Time": "12:22 AM",
        "Salary": 82744,
        "Senior Management": "true",
        "Start Date": "Wed, 08 Oct 2008 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "7.524",
        "First Name": "Frances",
        "Gender": "Female",
        "Last Login Time": "6:51 AM",
        "Salary": 139852,
        "Senior Management": "true",
        "Start Date": "Thu, 08 Aug 2002 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "4.709",
        "First Name": "Frances",
        "Gender": "Female",
        "Last Login Time": "4:19 PM",
        "Salary": 90582,
        "Senior Management": "true",
        "Start Date": "Sun, 04 Apr 1999 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "11.506",
        "First Name": "Frances",
        "Gender": "Female",
        "Last Login Time": "2:34 AM",
        "Salary": 91996,
        "Senior Management": "false",
        "Start Date": "Sat, 21 Jul 2001 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "1.433",
        "First Name": "Frances",
        "Gender": "Female",
        "Last Login Time": "6:08 PM",
        "Salary": 112467,
        "Senior Management": "false",
        "Start Date": "Tue, 12 Nov 1996 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "17.667",
        "First Name": "Frances",
        "Gender": "Female",
        "Last Login Time": "8:31 AM",
        "Salary": 35884,
        "Senior Management": "false",
        "Start Date": "Fri, 16 May 2014 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "14.166",
        "First Name": "Heather",
        "Gender": "Female",
        "Last Login Time": "2:17 PM",
        "Salary": 43026,
        "Senior Management": "false",
        "Start Date": "Sat, 11 Jul 1998 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "14.955",
        "First Name": "Heather",
        "Gender": "Female",
        "Last Login Time": "10:48 AM",
        "Salary": 47605,
        "Senior Management": "true",
        "Start Date": "Fri, 29 Jul 1983 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "19.343",
        "First Name": "Jessica",
        "Gender": "Female",
        "Last Login Time": "5:53 AM",
        "Salary": 68759,
        "Senior Management": "true",
        "Start Date": "Mon, 23 Oct 1995 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "6.388",
        "First Name": "Jessica",
        "Gender": "Female",
        "Last Login Time": "1:35 PM",
        "Salary": 75145,
        "Senior Management": "true",
        "Start Date": "Fri, 27 Sep 1985 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "13.591",
        "First Name": "Jessica",
        "Gender": "Female",
        "Last Login Time": "9:58 PM",
        "Salary": 90285,
        "Senior Management": "true",
        "Start Date": "Sun, 19 Oct 1986 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "14.752",
        "First Name": "Kathryn",
        "Gender": "Female",
        "Last Login Time": "1:47 PM",
        "Salary": 73935,
        "Senior Management": "false",
        "Start Date": "Wed, 04 Feb 2004 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "7.799",
        "First Name": "Kathryn",
        "Gender": "Female",
        "Last Login Time": "9:29 AM",
        "Salary": 86439,
        "Senior Management": "false",
        "Start Date": "Thu, 09 Jun 1988 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "11.864",
        "First Name": "Kathryn",
        "Gender": "Female",
        "Last Login Time": "6:10 AM",
        "Salary": 53061,
        "Senior Management": "true",
        "Start Date": "Wed, 29 Aug 2007 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "6.081",
        "First Name": "Kathryn",
        "Gender": "Female",
        "Last Login Time": "12:29 AM",
        "Salary": 86676,
        "Senior Management": "false",
        "Start Date": "Tue, 29 Jan 2008 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "18.015",
        "First Name": "Kathryn",
        "Gender": "Female",
        "Last Login Time": "3:39 PM",
        "Salary": 57300,
        "Senior Management": "false",
        "Start Date": "Fri, 27 Oct 1995 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "1.256",
        "First Name": "Lillian",
        "Gender": "Female",
        "Last Login Time": "6:09 AM",
        "Salary": 59414,
        "Senior Management": "false",
        "Start Date": "Sun, 05 Jun 2016 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "3.959",
        "First Name": "Lillian",
        "Gender": "Female",
        "Last Login Time": "6:51 PM",
        "Salary": 85446,
        "Senior Management": "true",
        "Start Date": "Sun, 21 Dec 2008 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "12.184",
        "First Name": "Lillian",
        "Gender": "Female",
        "Last Login Time": "4:44 PM",
        "Salary": 123940,
        "Senior Management": "true",
        "Start Date": "Sat, 19 Jun 1999 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "18.018",
        "First Name": "Lillian",
        "Gender": "Female",
        "Last Login Time": "5:41 AM",
        "Salary": 113554,
        "Senior Management": "true",
        "Start Date": "Fri, 14 Aug 2009 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "4.924",
        "First Name": "Lillian",
        "Gender": "Female",
        "Last Login Time": "8:53 AM",
        "Salary": 103854,
        "Senior Management": "true",
        "Start Date": "Mon, 26 Aug 2002 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "5.207",
        "First Name": "Marilyn",
        "Gender": "Female",
        "Last Login Time": "3:16 AM",
        "Salary": 73524,
        "Senior Management": "true",
        "Start Date": "Sun, 07 Dec 1980 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "2.401",
        "First Name": "Marilyn",
        "Gender": "Female",
        "Last Login Time": "8:29 AM",
        "Salary": 76078,
        "Senior Management": "true",
        "Start Date": "Wed, 16 Nov 1983 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "10.263",
        "First Name": "Marilyn",
        "Gender": "Female",
        "Last Login Time": "9:28 PM",
        "Salary": 147663,
        "Senior Management": "false",
        "Start Date": "Fri, 04 Apr 1997 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "2.937",
        "First Name": "Marilyn",
        "Gender": "Female",
        "Last Login Time": "2:23 AM",
        "Salary": 86386,
        "Senior Management": "false",
        "Start Date": "Sat, 26 Sep 1981 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "8.748",
        "First Name": "Marilyn",
        "Gender": "Female",
        "Last Login Time": "12:10 PM",
        "Salary": 147183,
        "Senior Management": "false",
        "Start Date": "Fri, 17 Dec 1982 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "9.989",
        "First Name": "Marilyn",
        "Gender": "Female",
        "Last Login Time": "9:14 AM",
        "Salary": 140502,
        "Senior Management": "true",
        "Start Date": "Tue, 15 Aug 1989 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "17.33",
        "First Name": "Marilyn",
        "Gender": "Female",
        "Last Login Time": "11:24 AM",
        "Salary": 87145,
        "Senior Management": "false",
        "Start Date": "Wed, 09 Aug 2006 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "2.924",
        "First Name": "Marilyn",
        "Gender": "Female",
        "Last Login Time": "4:06 PM",
        "Salary": 92430,
        "Senior Management": "false",
        "Start Date": "Mon, 02 Jul 1984 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "11.934",
        "First Name": "Marilyn",
        "Gender": "Female",
        "Last Login Time": "12:32 AM",
        "Salary": 115149,
        "Senior Management": "true",
        "Start Date": "Mon, 08 Oct 2007 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "7.696",
        "First Name": "Marilyn",
        "Gender": "Female",
        "Last Login Time": "7:18 AM",
        "Salary": 118369,
        "Senior Management": "true",
        "Start Date": "Tue, 16 Jan 1996 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "14.995",
        "First Name": "Melissa",
        "Gender": "Female",
        "Last Login Time": "6:33 AM",
        "Salary": 48109,
        "Senior Management": "false",
        "Start Date": "Tue, 21 Jun 2005 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "3.525",
        "First Name": "Melissa",
        "Gender": "Female",
        "Last Login Time": "4:11 AM",
        "Salary": 98858,
        "Senior Management": "true",
        "Start Date": "Thu, 08 Sep 1994 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "8.879",
        "First Name": "Melissa",
        "Gender": "Female",
        "Last Login Time": "1:20 AM",
        "Salary": 45223,
        "Senior Management": "true",
        "Start Date": "Tue, 22 Oct 2002 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "10.256",
        "First Name": "Mildred",
        "Gender": "Female",
        "Last Login Time": "3:30 AM",
        "Salary": 47266,
        "Senior Management": "false",
        "Start Date": "Sat, 21 Feb 1981 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "11.39",
        "First Name": "Mildred",
        "Gender": "Female",
        "Last Login Time": "10:06 PM",
        "Salary": 139284,
        "Senior Management": "true",
        "Start Date": "Fri, 06 Apr 2007 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "8.932",
        "First Name": "Phyllis",
        "Gender": "Female",
        "Last Login Time": "9:30 PM",
        "Salary": 136984,
        "Senior Management": "true",
        "Start Date": "Fri, 11 Oct 1996 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "8.723",
        "First Name": "Phyllis",
        "Gender": "Female",
        "Last Login Time": "11:57 PM",
        "Salary": 140347,
        "Senior Management": "false",
        "Start Date": "Thu, 24 Nov 2005 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "16.697",
        "First Name": "Phyllis",
        "Gender": "Female",
        "Last Login Time": "5:27 AM",
        "Salary": 125881,
        "Senior Management": "false",
        "Start Date": "Sun, 15 Jan 1995 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "17.517",
        "First Name": "Rebecca",
        "Gender": "Female",
        "Last Login Time": "12:23 AM",
        "Salary": 94231,
        "Senior Management": "false",
        "Start Date": "Fri, 10 Jul 1992 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "5.359",
        "First Name": "Rebecca",
        "Gender": "Female",
        "Last Login Time": "4:13 AM",
        "Salary": 85730,
        "Senior Management": "true",
        "Start Date": "Sat, 15 Nov 1980 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "4.443",
        "First Name": "Rebecca",
        "Gender": "Female",
        "Last Login Time": "6:50 AM",
        "Salary": 109259,
        "Senior Management": "true",
        "Start Date": "Sat, 18 Feb 1995 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "6.878",
        "First Name": "Rebecca",
        "Gender": "Female",
        "Last Login Time": "3:21 PM",
        "Salary": 134673,
        "Senior Management": "false",
        "Start Date": "Fri, 23 Feb 1990 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "11.367",
        "First Name": "Rebecca",
        "Gender": "Female",
        "Last Login Time": "10:33 AM",
        "Salary": 46750,
        "Senior Management": "true",
        "Start Date": "Sun, 05 Mar 2000 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "16.135",
        "First Name": "Shirley",
        "Gender": "Female",
        "Last Login Time": "10:39 PM",
        "Salary": 147113,
        "Senior Management": "false",
        "Start Date": "Wed, 20 Jun 2001 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "6.219",
        "First Name": "Shirley",
        "Gender": "Female",
        "Last Login Time": "1:15 PM",
        "Salary": 41334,
        "Senior Management": "true",
        "Start Date": "Tue, 01 May 1984 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "1.854",
        "First Name": "Shirley",
        "Gender": "Female",
        "Last Login Time": "1:23 PM",
        "Salary": 113850,
        "Senior Management": "false",
        "Start Date": "Sat, 28 Feb 1981 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "7.494",
        "First Name": "Shirley",
        "Gender": "Female",
        "Last Login Time": "2:25 AM",
        "Salary": 110061,
        "Senior Management": "false",
        "Start Date": "Sun, 08 Jun 1986 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "2.754",
        "First Name": "Shirley",
        "Gender": "Female",
        "Last Login Time": "11:09 AM",
        "Salary": 132156,
        "Senior Management": "false",
        "Start Date": "Sat, 16 Apr 1988 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "16.675",
        "First Name": "Theresa",
        "Gender": "Female",
        "Last Login Time": "1:12 AM",
        "Salary": 85182,
        "Senior Management": "false",
        "Start Date": "Tue, 10 Oct 2006 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "1.481",
        "First Name": "Theresa",
        "Gender": "Female",
        "Last Login Time": "7:18 AM",
        "Salary": 72670,
        "Senior Management": "true",
        "Start Date": "Sun, 11 Apr 2010 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "1.079",
        "First Name": "Theresa",
        "Gender": "Female",
        "Last Login Time": "9:17 PM",
        "Salary": 75661,
        "Senior Management": "true",
        "Start Date": "Fri, 27 Apr 2001 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "13.079",
        "First Name": "Jennifer",
        "Gender": "Female",
        "Last Login Time": "10:47 PM",
        "Salary": 71715,
        "Senior Management": "true",
        "Start Date": "Sat, 04 Apr 2009 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "10.006",
        "First Name": "Jennifer",
        "Gender": "Female",
        "Last Login Time": "7:43 PM",
        "Salary": 132084,
        "Senior Management": "true",
        "Start Date": "Tue, 31 Mar 2015 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "14.595",
        "First Name": "Kathleen",
        "Gender": "Female",
        "Last Login Time": "9:16 AM",
        "Salary": 35575,
        "Senior Management": "false",
        "Start Date": "Fri, 13 Jun 2014 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "8.572",
        "First Name": "Kathleen",
        "Gender": "Female",
        "Last Login Time": "3:45 PM",
        "Salary": 71430,
        "Senior Management": "false",
        "Start Date": "Fri, 20 Sep 1996 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "3.756",
        "First Name": "Kathleen",
        "Gender": "Female",
        "Last Login Time": "10:49 AM",
        "Salary": 42553,
        "Senior Management": "true",
        "Start Date": "Sat, 28 Aug 2004 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "14.543",
        "First Name": "Kimberly",
        "Gender": "Female",
        "Last Login Time": "7:13 AM",
        "Salary": 41426,
        "Senior Management": "true",
        "Start Date": "Thu, 14 Jan 1999 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "7.953",
        "First Name": "Kimberly",
        "Gender": "Female",
        "Last Login Time": "5:57 AM",
        "Salary": 36643,
        "Senior Management": "false",
        "Start Date": "Tue, 15 Jul 1997 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "5.435",
        "First Name": "Kimberly",
        "Gender": "Female",
        "Last Login Time": "4:51 AM",
        "Salary": 81800,
        "Senior Management": "true",
        "Start Date": "Wed, 30 Dec 1981 00:00:00 GMT",
        "Team": "null"
    },
    {
        "Bonus %": "12.929",
        "First Name": "Kimberly",
        "Gender": "Female",
        "Last Login Time": "2:23 PM",
        "Salary": 37916,
        "Senior Management": "true",
        "Start Date": "Sat, 06 Dec 1986 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "4.513",
        "First Name": "Kimberly",
        "Gender": "Female",
        "Last Login Time": "3:55 PM",
        "Salary": 52970,
        "Senior Management": "false",
        "Start Date": "Sun, 20 Apr 1986 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "8.862",
        "First Name": "Kimberly",
        "Gender": "Female",
        "Last Login Time": "12:57 AM",
        "Salary": 46233,
        "Senior Management": "true",
        "Start Date": "Sat, 26 Jan 2013 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "7.353",
        "First Name": "Margaret",
        "Gender": "Female",
        "Last Login Time": "12:42 PM",
        "Salary": 131604,
        "Senior Management": "true",
        "Start Date": "Sat, 10 Sep 1988 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "3.733",
        "First Name": "Margaret",
        "Gender": "Female",
        "Last Login Time": "1:05 PM",
        "Salary": 125220,
        "Senior Management": "false",
        "Start Date": "Sat, 06 Feb 1993 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "4.078",
        "First Name": "Margaret",
        "Gender": "Female",
        "Last Login Time": "6:01 AM",
        "Salary": 55044,
        "Senior Management": "false",
        "Start Date": "Mon, 05 May 2014 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "1.552",
        "First Name": "Margaret",
        "Gender": "Female",
        "Last Login Time": "3:07 AM",
        "Salary": 126924,
        "Senior Management": "true",
        "Start Date": "Thu, 04 Jan 2001 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "17.179",
        "First Name": "Michelle",
        "Gender": "Female",
        "Last Login Time": "6:43 PM",
        "Salary": 57325,
        "Senior Management": "true",
        "Start Date": "Fri, 30 Mar 1984 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "5.455",
        "First Name": "Michelle",
        "Gender": "Female",
        "Last Login Time": "9:34 PM",
        "Salary": 53754,
        "Senior Management": "true",
        "Start Date": "Mon, 04 Nov 1996 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "14.226",
        "First Name": "Patricia",
        "Gender": "Female",
        "Last Login Time": "6:46 AM",
        "Salary": 49368,
        "Senior Management": "false",
        "Start Date": "Mon, 01 Sep 2003 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "4.15",
        "First Name": "Patricia",
        "Gender": "Female",
        "Last Login Time": "2:24 AM",
        "Salary": 95322,
        "Senior Management": "false",
        "Start Date": "Wed, 25 Nov 1992 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "8.399",
        "First Name": "Patricia",
        "Gender": "Female",
        "Last Login Time": "4:01 AM",
        "Salary": 114079,
        "Senior Management": "true",
        "Start Date": "Thu, 06 Dec 2012 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "16.624",
        "First Name": "Patricia",
        "Gender": "Female",
        "Last Login Time": "4:16 AM",
        "Salary": 121232,
        "Senior Management": "false",
        "Start Date": "Fri, 09 Jan 2015 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "7.839",
        "First Name": "Patricia",
        "Gender": "Female",
        "Last Login Time": "1:10 AM",
        "Salary": 75825,
        "Senior Management": "false",
        "Start Date": "Sat, 07 Mar 1998 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "6.911",
        "First Name": "Patricia",
        "Gender": "Female",
        "Last Login Time": "4:52 PM",
        "Salary": 119266,
        "Senior Management": "false",
        "Start Date": "Tue, 10 Oct 1995 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "19.154",
        "First Name": "Virginia",
        "Gender": "Female",
        "Last Login Time": "6:23 AM",
        "Salary": 46905,
        "Senior Management": "false",
        "Start Date": "Wed, 20 Oct 1999 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "10.154",
        "First Name": "Virginia",
        "Gender": "Female",
        "Last Login Time": "9:10 PM",
        "Salary": 123649,
        "Senior Management": "true",
        "Start Date": "Sun, 02 May 2010 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "14.858",
        "First Name": "Catherine",
        "Gender": "Female",
        "Last Login Time": "7:24 PM",
        "Salary": 58047,
        "Senior Management": "true",
        "Start Date": "Sat, 31 Aug 2013 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "12.801",
        "First Name": "Catherine",
        "Gender": "Female",
        "Last Login Time": "6:20 PM",
        "Salary": 59970,
        "Senior Management": "false",
        "Start Date": "Sun, 31 Aug 1986 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "18.393",
        "First Name": "Catherine",
        "Gender": "Female",
        "Last Login Time": "1:31 AM",
        "Salary": 68164,
        "Senior Management": "false",
        "Start Date": "Mon, 25 Sep 1989 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "9.096",
        "First Name": "Christina",
        "Gender": "Female",
        "Last Login Time": "1:19 PM",
        "Salary": 118780,
        "Senior Management": "true",
        "Start Date": "Tue, 06 Aug 2002 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "13.892",
        "First Name": "Christina",
        "Gender": "Female",
        "Last Login Time": "2:04 PM",
        "Salary": 110169,
        "Senior Management": "true",
        "Start Date": "Fri, 13 Apr 2012 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "18.178",
        "First Name": "Christina",
        "Gender": "Female",
        "Last Login Time": "3:18 PM",
        "Salary": 35477,
        "Senior Management": "false",
        "Start Date": "Sun, 23 Jun 2002 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "11.996",
        "First Name": "Christine",
        "Gender": "Female",
        "Last Login Time": "4:01 AM",
        "Salary": 94345,
        "Senior Management": "false",
        "Start Date": "Mon, 03 Jul 1989 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "11.126",
        "First Name": "Christine",
        "Gender": "Female",
        "Last Login Time": "1:11 PM",
        "Salary": 72613,
        "Senior Management": "false",
        "Start Date": "Sat, 01 Feb 2003 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "5.687",
        "First Name": "Elizabeth",
        "Gender": "Female",
        "Last Login Time": "5:53 PM",
        "Salary": 146129,
        "Senior Management": "false",
        "Start Date": "Thu, 09 Oct 2003 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "1.782",
        "First Name": "Elizabeth",
        "Gender": "Female",
        "Last Login Time": "4:56 AM",
        "Salary": 106406,
        "Senior Management": "true",
        "Start Date": "Thu, 10 Nov 2005 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "19.78",
        "First Name": "Elizabeth",
        "Gender": "Female",
        "Last Login Time": "7:02 AM",
        "Salary": 79145,
        "Senior Management": "false",
        "Start Date": "Sun, 21 Feb 2010 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "10.081",
        "First Name": "Elizabeth",
        "Gender": "Female",
        "Last Login Time": "11:12 AM",
        "Salary": 137144,
        "Senior Management": "false",
        "Start Date": "Mon, 27 Jul 1998 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "1.767",
        "First Name": "Katherine",
        "Gender": "Female",
        "Last Login Time": "8:15 AM",
        "Salary": 57531,
        "Senior Management": "false",
        "Start Date": "Sun, 14 Nov 1999 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "18.912",
        "First Name": "Katherine",
        "Gender": "Female",
        "Last Login Time": "12:21 AM",
        "Salary": 149908,
        "Senior Management": "false",
        "Start Date": "Tue, 13 Aug 1996 00:00:00 GMT",
        "Team": "Finance"
    },
    {
        "Bonus %": "4.659",
        "First Name": "Katherine",
        "Gender": "Female",
        "Last Login Time": "1:40 AM",
        "Salary": 41643,
        "Senior Management": "true",
        "Start Date": "Tue, 19 Dec 2000 00:00:00 GMT",
        "Team": "Distribution"
    },
    {
        "Bonus %": "13.178",
        "First Name": "Katherine",
        "Gender": "Female",
        "Last Login Time": "8:08 PM",
        "Salary": 72002,
        "Senior Management": "true",
        "Start Date": "Fri, 22 Sep 2006 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "13.657",
        "First Name": "Katherine",
        "Gender": "Female",
        "Last Login Time": "3:58 PM",
        "Salary": 97443,
        "Senior Management": "false",
        "Start Date": "Sun, 18 Aug 2013 00:00:00 GMT",
        "Team": "Product"
    },
    {
        "Bonus %": "5.574",
        "First Name": "Stephanie",
        "Gender": "Female",
        "Last Login Time": "1:52 AM",
        "Salary": 36844,
        "Senior Management": "true",
        "Start Date": "Sat, 13 Sep 1986 00:00:00 GMT",
        "Team": "Business Development"
    },
    {
        "Bonus %": "13.218",
        "First Name": "Stephanie",
        "Gender": "Female",
        "Last Login Time": "11:15 AM",
        "Salary": 50141,
        "Senior Management": "true",
        "Start Date": "Thu, 24 Mar 1983 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "7.937",
        "First Name": "Stephanie",
        "Gender": "Female",
        "Last Login Time": "12:54 AM",
        "Salary": 122121,
        "Senior Management": "true",
        "Start Date": "Thu, 26 Nov 1992 00:00:00 GMT",
        "Team": "Engineering"
    },
    {
        "Bonus %": "3.453",
        "First Name": "Stephanie",
        "Gender": "Female",
        "Last Login Time": "8:14 AM",
        "Salary": 96649,
        "Senior Management": "false",
        "Start Date": "Tue, 14 Sep 1982 00:00:00 GMT",
        "Team": "Sales"
    },
    {
        "Bonus %": "6.16",
        "First Name": "Stephanie",
        "Gender": "Female",
        "Last Login Time": "5:48 AM",
        "Salary": 136604,
        "Senior Management": "true",
        "Start Date": "Sun, 26 Jun 1988 00:00:00 GMT",
        "Team": "Human Resources"
    },
    {
        "Bonus %": "18.243",
        "First Name": "Jacqueline",
        "Gender": "Female",
        "Last Login Time": "3:01 PM",
        "Salary": 145988,
        "Senior Management": "false",
        "Start Date": "Wed, 25 Nov 1981 00:00:00 GMT",
        "Team": "Marketing"
    },
    {
        "Bonus %": "14.609",
        "First Name": "Jacqueline",
        "Gender": "Female",
        "Last Login Time": "2:01 AM",
        "Salary": 66604,
        "Senior Management": "false",
        "Start Date": "Sun, 11 Feb 2007 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "15.77",
        "First Name": "Jacqueline",
        "Gender": "Female",
        "Last Login Time": "6:07 PM",
        "Salary": 62371,
        "Senior Management": "true",
        "Start Date": "Tue, 20 Sep 1994 00:00:00 GMT",
        "Team": "Client Services"
    },
    {
        "Bonus %": "3.019",
        "First Name": "Jacqueline",
        "Gender": "Female",
        "Last Login Time": "12:08 PM",
        "Salary": 125298,
        "Senior Management": "true",
        "Start Date": "Sun, 27 Jul 2008 00:00:00 GMT",
        "Team": "Legal"
    },
    {
        "Bonus %": "8.064",
        "First Name": "Jacqueline",
        "Gender": "Female",
        "Last Login Time": "7:13 PM",
        "Salary": 125418,
        "Senior Management": "false",
        "Start Date": "Sun, 25 May 2003 00:00:00 GMT",
        "Team": "Distribution"
    }
]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug="true", host="0.0.0.0")
