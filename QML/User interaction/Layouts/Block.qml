import QtQuick 2.15

Item {
    property alias comText: txt.text
    Rectangle {
        id: content
        width: parent
        height: parent
        color: "transparent"
        border.color: "gray"
        border.width: 1
        anchors.centerIn: parent
        Text {
            id: txt
            text: ""
            anchors.centerIn: parent
        }
    }
}
