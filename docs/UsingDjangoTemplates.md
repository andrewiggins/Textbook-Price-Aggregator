Django Templates
================

Google App Engine [comes with][Google App Engine Templates] the [Django 1.2 Template Engine][Template Reference] built-in. 

Django Templates allows us to write HTML files that include special tags that allow us to apply logic to the html tags that we evaluate before sending to the user. So we can design HTML files with loops, if else blocks, and inheritance very easily. Also, we can apply filters to text we output into the HTML such as `escape` which escapes the code before writing it. Use the [template reference] page to see the available tags and filters.

Two parts of the reference to take note of:

1. [Template Inheritance]
2. [Automatic HTML Escaping]

Here is an example Django Template:

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang='en' lang='en'> 
    <head> 
      <meta http-equiv="content-type" content="text/html; charset=UTF-8" /> 
      <link rel="stylesheet" type="text/css" href="/stylesheets/songtable.css" />
      <style type="text/css">
      td.flag_true {
        color:#FF0000;
      }
    
      td.updated_True {
        color:#00FF00;
      }
    
      td.updated_New {
        color:#0000FF;
      }
      </style>
      
      <script type="text/javascript" src="/scripts/audio.js"></script>
      
      <title>{{ title }}
      {% for chart in charts %}
        {% if forloop.last %}
          {{ chart.title|title }}
        {% else %}
          {{ chart.title|title }}, 
        {% endif %}
      {% endfor %}
      </title> 
    </head> 
     
    <body onload="onLoad();"> 
      <div class="login">
        <a href="{{ login_url }}">{{ login_url_linktext }}</a>
      </div>
    
      {% for chart in charts %}
      <h1>{{ chart.title|title }}</h1>
      
      <table class="songs">
        
      <thead> 
        <tr class="headers">
          <th class="ranking"></th>
          <th class="title">Song Title</th>
          <th class="artist">Artist</th>
          <th class="album">Album</th>
          <th class="flag">Flagged</th>
          {% ifequal title "Update" %}
          <th class="updated">Updated</th>
          {% endifequal %}
          <th class="iLikeUrl">iLike Link</th>
        </tr>
      </thead>
      
      <tbody>
        {% for song in chart.songs %}
        <tr class="song_{% cycle row1,row2 %}" >
          <td class="ranking">{{ song.rank }}.</td>
          <td class="title">{{ song.title }}</td>
          <td class="artist">{{ song.artist }}</td>
          <td class="album">{{ song.album }}</td>
          
          {% if song.flag %}
          <td class="flag_true" title="{{ song.message }}">True</td>
          {% else%}
          <td class="flag_false">False</td>
          {% endif %}
          {% ifequal title "Update" %}
          <td class="updated_{{ song.updated }}">{{ song.updated }}</td>
          {% endifequal %}
          <td class="iLikeUrl">
          {% if song.iLikeUrl %}
            <a name="{{ song.key_id }}" id="{{ song.key_id }}_button" class="song_play_btn"
              onclick="PlaySong(this.id);" href="javascript: void(0);"
            ></a>
            <audio name="{{ song.key_id }}" id="{{ song.key_id }}_audio" type="{{ song.src }}">
              <source src="{{ song.iLikeUrl }}" type="audio/mpeg" />
            </audio>
            <a href="{{ song.iLikeUrl }}">{{ song.iLikeUrl }}</a>
          {% else %}
            {{ song.iLikeUrl }}
          {% endif %}
          </td>
          
        </tr>
        {% endfor %}
      </tbody>
        
      </table>
      {% endfor %}
        
    </body> 
    </html>

[Google App Engine Templates]: http://code.google.com/appengine/docs/python/gettingstarted/templates.html "Google App Engine Templates"
[Template Reference]: http://docs.djangoproject.com/en/1.2/ref/templates/builtins/ "Django 1.2 Template Reference"
[Template Inheritance]: http://docs.djangoproject.com/en/1.2/topics/templates/#template-inheritance "Django 1.2 Template Inheritance"
[Automatic HTML Escaping]: http://docs.djangoproject.com/en/1.2/topics/templates/#automatic-html-escaping "Django 1.2 Automatic HTML Escaping"