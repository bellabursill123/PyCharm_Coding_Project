import folium

m = folium.Map(location=[-37.846979, 144.970814], zoom_start=15)

folium.Marker(location=[-37.85002883485026, 144.9690284450483],
              popup="<h1> Starting Line </h1><img src='Starting Line.png' width=400px><p style='font-size: 18px;'>The start and finish line for all drivers.</p>",
              icon=folium.Icon(icon_color='lightgreen', color='black', icon='fas fa-flag-checkered', prefix='fa'),
              tooltip='Start/Finish Line').add_to(m)

folium.Marker(location=[-37.847591, 144.965980],
              popup="<h1> Turn 1 </h1><img src='turn1.jpg' width=300px><p style='font-size: 18px;'>The first turn.</p>",
              icon=folium.Icon(icon_color='red', color='black', icon='fas fa-1', prefix='fa'),
              tooltip='T1').add_to(m)

folium.Marker(location=[-37.846579, 144.966209],
              popup="<h1> Turn 2 </h1><img src='turn 2 new.png' width=300px><p style='font-size: 18px;'> The second turn.</p>",
              icon=folium.Icon(icon_color='red', color='black', icon='fas fa-2', prefix='fa'),
              tooltip='T2').add_to(m)

folium.Marker(location=[-37.842181, 144.962152],
              popup="<h1> Turn 3 </h1><img src='turn3.png' width=300px><p style='font-size: 18px;'> The third turn.</p>",
              icon=folium.Icon(icon_color='red', color='black', icon='fas fa-3', prefix='fa'),
              tooltip='T3').add_to(m)

folium.Marker(location=[-37.841772, 144.963725],
              popup="<h1> Turn 4 </h><img src='turn4.png' width=300px><p style='font-size: 18px;'> The fourth turn.</p>",
              icon=folium.Icon(icon_color='red', color='black', icon='fas fa-4', prefix='fa'),
              tooltip='T4').add_to(m)

folium.Marker(location=[-37.839860, 144.963692],
              popup="<h1> Turn 5 </h><img src='turn5.png' width=300px><p style='font-size: 18px;'> The fifth turn.</p>",
              icon=folium.Icon(icon_color='red', color='black', icon='fas fa-5', prefix='fa'),
              tooltip='T5').add_to(m)

folium.Marker(location=[-37.838035, 144.967916],
              popup="<h1> Turn 6 </h><img src='turn6.jpeg' width=300px><p style='font-size: 18px;'> The sixth turn.</p>",
              icon=folium.Icon(icon_color='#3e82e5', color='black', icon='fas fa-6', prefix='fa'),
              tooltip='T6').add_to(m)

folium.Marker(location=[-37.838420, 144.968419],
              popup="<h1> Turn 7 </h><img src='turn7.png' width=300px><p style='font-size: 18px;'> The seventh turn.</p>",
              icon=folium.Icon(icon_color='#3e82e5', color='black', icon='fas fa-7', prefix='fa'),
              tooltip='T7').add_to(m)

folium.Marker(location=[-37.838594, 144.969515],
              popup="<h1> Turn 8 </h><img src='turn8.png' width=300px><p style='font-size: 18px;'> The eighth turn.</p>",
              icon=folium.Icon(icon_color='#3e82e5', color='black', icon='fas fa-8', prefix='fa'),
              tooltip='T8').add_to(m)

folium.Marker(location=[-37.848152, 144.973430],
              popup="<h1> Turn 9 </h><img src='turn9.png' width=300px><p style='font-size: 18px;'> The ninth turn.</p>",
              icon=folium.Icon(icon_color='yellow', color='black', icon='fas fa-newspaper', prefix='fa'),
              tooltip='T9').add_to(m)

folium.Marker(location=[-37.848225, 144.974714],
              popup="<h1> Turn 10 </h1><img src='turn10.png' width=300px><p style='font-size: 18px;'>The tenth turn.</p>",
              icon=folium.Icon(icon_color='yellow', color='black', icon='fas fa-tree', prefix='fa'),
              tooltip='T10').add_to(m)

folium.Marker(location=[-37.853136, 144.978465],
              popup="<h1> Turn 11 </h1><img src='turn11.png' width=300px><p style='font-size: 18px;'>The eleventh turn.</p>",
              icon=folium.Icon(icon_color='yellow', color='black', icon='fas fa-envelope', prefix='fa'),
              tooltip='T11').add_to(m)

folium.Marker(location=[-37.853828, 144.975613],
              popup="<h1> Turn 12 </h1><img src='turn12.png' width=300px><p style='font-size: 18px;'>The twelfth turn.</p>",
              icon=folium.Icon(icon_color='yellow', color='black', icon='fas fa-truck-fast', prefix='fa'),
              tooltip='T12').add_to(m)

folium.Marker(location=[-37.852091, 144.974124],
              popup="<h1> Turn 13 </h1><img src='turn13.png' width=300px><p style='font-size: 18px;'>The thirteenth turn.</p>",
              icon=folium.Icon(icon_color='yellow', color='black', icon='fas fa-trophy', prefix='fa'),
              tooltip='T13').add_to(m)

folium.Marker(location=[-37.852886, 144.972951],
              popup="<h1> Turn 14 </h1><img src='turn14.png' width=300px><p style='font-size: 18px;'>The fourteenth turn.</p>",
              icon=folium.Icon(icon_color='yellow', color='black', icon='fas fa-fish', prefix='fa'),
              tooltip='T14').add_to(m)

folium.Marker(location=[-37.842567, 144.969073],
              icon=folium.Icon(icon_color='white', color='black', icon='fas fa-info', prefix='fa'),
              tooltip='An informational sector explaining the meanings of icons and colours',
              popup=folium.Popup(html="<h1> Key </h1><p style='font-size: 18px;'>Sectors: <br>o Red = Sector 1 "
                                      "<br>o Blue = Sector 2 "
                                      "<br>o Yellow = Sector 3"
                                      "<br><br> DRS Zones:"
                                      "<br>o DRS Zones are the dotted orange lines, which stands for 'Drag Reduction System' During these zones, drivers can enable their DRS on their cars which makes them go faster. Thus encouraging more overtaking and a more interesting and action packed race."
                                      "<br><br> Icons:"
                                      "<br>o Newspaper = Turn 9 "
                                      "<br>o Tree = Turn 10 "
                                      "<br>o Envelope = Turn 11 "
                                      "<br>o Truck = Turn 12 "
                                      "<br>o Trophy = Turn 13 "
                                      "<br>o Fish = Turn 14</p>",max_width=400)
              ).add_to(m)

line_coordinates = [
    [-37.852801, 144.972264],
    [-37.847757, 144.965907]
]
folium.PolyLine(locations=line_coordinates, color='#FF5733', weight=4, opacity=7, dash_array='5,10').add_to(m)

line_coordinates2 = [
    [-37.846302, 144.965888],
    [-37.845807, 144.965195],
    [-37.844782, 144.963984],
    [-37.843734, 144.963032],
    [-37.842960, 144.962426],
    [-37.842368, 144.962066]
]
folium.PolyLine(locations=line_coordinates2, color='#FF5733', weight=4, opacity=7, dash_array='5,10').add_to(m)

line_coordinates3 = [

    [-37.845266, 144.970862],
    [-37.846096, 144.971118],
    [-37.846867, 144.971854],
    [-37.847268, 144.972343],
    [-37.847872, 144.973302],
]
folium.PolyLine(locations=line_coordinates3, color='#FF5733', weight=4, opacity=7, dash_array='5,10').add_to(m)

line_coordinates4 = [
    [-37.848737, 144.976079],
    [-37.849191, 144.976776],
    [-37.849717, 144.977396],
    [-37.850303, 144.977805],
    [-37.851271, 144.978123],
    [-37.852144, 144.978410],
    [-37.853028, 144.978638]
]
folium.PolyLine(locations=line_coordinates4, color='#FF5733', weight=4, opacity=7, dash_array='5,10').add_to(m)



m.save('map.html')
