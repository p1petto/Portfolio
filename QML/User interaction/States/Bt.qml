import QtQuick 2.15
import QtQuick.Layouts 1.3

Item {
    property alias comColor: rect1.color
    property alias comText: txt.text
    property alias comColorText: txt.color

    Layout.fillWidth: true
    Layout.fillHeight: parent

    Rectangle {
        id: rect1
        width: parent.width
        height: parent.height
        color: '#A5A5A5'
        Text {
            id: txt
            text: "1"
            anchors.centerIn: parent
            color: "black"
        }
    }
}
