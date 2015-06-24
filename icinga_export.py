import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)
dbc = mysql.connector.connect(user='icinga_read', password='Ax1sGW', host='192.168.0.202', database='icinga')

@app.route('/services')
def view_services():
    cursor = dbc.cursor()
    cursor.execute("SELECT "
                   "icinga_hosts.display_name AS host_name, "
                   "icinga_services.display_name as service_name, "
                   "icinga_servicestatus.current_state as service_state "
                   "FROM icinga_servicestatus "
                   "JOIN icinga_services ON icinga_servicestatus.service_object_id = icinga_services.service_object_id "
                   "JOIN icinga_hosts ON icinga_services.host_object_id = icinga_hosts.host_object_id "
                   "WHERE icinga_servicestatus.status_update_time >= DATE_SUB(NOW(), INTERVAL 1 HOUR)")
    i_host_name = cursor.column_names.index("host_name")
    i_service_name = cursor.column_names.index("service_name")
    i_service_state = cursor.column_names.index("service_state")
    result = cursor.fetchall()

    d = []

    for row in result:
        print(str(row[i_host_name]) + "-" + str(row[i_service_name] + ": " + str(row[i_service_state])))
        d.append({'host_name': row[i_host_name], 'service_name': row[i_service_name], 'service_state': row[i_service_state]})
    return jsonify(services=d)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
