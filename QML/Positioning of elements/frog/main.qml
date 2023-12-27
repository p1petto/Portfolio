import QtQuick 2.15
import QtQuick.Window 2.15

Window {
    width: 640
    height: 480
    minimumWidth: 640
    minimumHeight: 480
    visible: true
    title: qsTr("Hello World")

    Circle{
        comColor: 'green'
        id: head_of_frog
        width: 200
        height: 200
        anchors.centerIn: parent
        Mouth {
            width: parent.width / 2
            height: parent.width / 2
            anchors.centerIn: parent
        }
    }

    Circle{
        comColor: 'green'
        id: left_eye
        width: 80
        height: 80
        anchors.left: head_of_frog.left
        anchors.verticalCenter: head_of_frog.top

        Circle {
            comColor: 'white'
            width: parent.width / 1.5
            height: parent.width / 1.5
            anchors.centerIn: parent
            Circle{
                comColor: 'black'
                width: parent.width / 2
                height: parent.width / 2
                anchors.centerIn: parent
            }
        }
    }

    Circle{
        comColor: 'green'
        id: right_eye
        width: 80
        height: 80
        anchors.right: head_of_frog.right
        anchors.verticalCenter: head_of_frog.top

        Circle {
            comColor: 'white'
            width: parent.width / 1.5
            height: parent.width / 1.5
            anchors.centerIn: parent
            Circle{
                comColor: 'black'
                width: parent.width / 2
                height: parent.width / 2
                anchors.centerIn: parent
            }
        }
    }

}
