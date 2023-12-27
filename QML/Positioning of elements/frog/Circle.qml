import QtQuick 2.15

Item {
    property alias comColor: rect1.color
    Rectangle {
        id: rect1
        width: parent.width
        height: parent.width
        radius: parent.width / 2
    }
}
